# Test Case – TCP Stream Reassembly and Fragmented Payload Detection

## 1. Goal

To validate the impact of TCP stream reassembly on detecting fragmented payloads especially when traffic is deliberately split to evade content-based detection mechanisms.

---

## 2. Why It Matters

IDS/IPS engines that analyze packets in isolation often fail to detect malicious payloads spread across multiple TCP segments. This evasion technique is frequently used in real-world attacks.

When reassembly is enabled, the IDS can reconstruct the complete stream and apply content-based detection more effectively.

This test allows me to confirm that stream reassembly is not just a theoretical feature, but a critical part of how modern engines parse and match data.

---

## 3. Checklist

What I wanted to understand and validate:

- [x] Whether the `http.uri` field appears with and without reassembly
- [x] If the string `/evil.js` can be detected when split across two TCP packets
- [x] If the rule `content: "/evil.js"` triggers an alert in both scenarios
- [x] How Suricata's `eve.json` behaves with and without TCP stream reconstruction
- [x] How to use Scapy to create split TCP payloads
- [x] How to replay this traffic across a real network using `tcpreplay`
- [x] How the Suricata engine (running in pfSense) sees this traffic in real-time

---

## 4. Setup

### Network Recap

| Machine        | IP               | Role                    |
|----------------|------------------|-------------------------|
| pfSense        | 192.168.100.1    | Gateway + IDS (Suricata)|
| Kali Linux     | 192.168.100.20   | Attacker/Traffic source |

Traffic generated from Kali is routed through pfSense via NAT ↔ LAN forwarding rules. Although Kali is connected to NAT, it can reach 192.168.100.1 thanks to specific routing rules in pfSense.

---

### Required Software

- **On Kali:**
  - Python 3.x with Scapy → `apt install python3-scapy`
  chat gera o link para a img: install_scapy
  - `tcpreplay` → install with `sudo apt install tcpreplay`
  img: install_tcpreplay
- **On pfSense:**
  - Suricata must be running on the **WAN interface**
        - Tem que rodar na wan, pq o kali vem pela interface wan

## 5. Rule Setup

### Step 1 — Create detection rule

- **On pfSense:**
    -
    Tive que acessar o site: https://docs.suricata.io/en/latest/rule-management/suricata-update.html
    ler isso no site e entender como faz para configurar e instalar as propias rules no suricata.
 
While it is possible to download and install rules manually, it is recommended to use a management tool for this. suricata-update is the official way to update and manage rules for Suricata.

To download the Emerging Threats Open ruleset, it is enough to simply run:
```bash
sudo suricata-update
```
This will download the ruleset into /var/lib/suricata/rules/

Suricata's configuration will have to be updated to have a rules config like this:
```bash
default-rule-path: /var/lib/suricata/rules
rule-files:
  - suricata.rules
```


```bash
/var/lib/suricata/rules
```

```bash
vim forgesec.rules
```

Add:

```
alert http any any -> any any (msg:"Detected /evil.js"; content:"/evil.js"; sid:1000001;)
```
igm: create_forgesec_rules
img: forgesec_rules

Adicionei o forgesec.rules ao suricata.yaml da interface em0
img:forgesec_rules_em0
suricata-update

verifiquei se a regra estava ativa via interface grafica
img:forgesec_rule_gui

This rule detects any occurrence of `/evil.js` in HTTP traffic — **but it only works** if the content is visible after reassembly.

  - Only the custom rule `/evil.js` should be active (to eliminate noise)
---

## 6. Payload Creation

### Step 1 — Create the test folder

```bash
mkdir -p ~/Desktop/ForgeSec/tests/IDS_00__tcp-stream-reassembly
cd ~/Desktop/ForgeSec/tests/IDS_00__tcp-stream-reassembly
```

### Step 2 — Write the Scapy script

```bash
nano generate_payload.py
```

Paste this:

```python
from scapy.all import *

ip = IP(dst="192.168.100.1")
tcp = TCP(sport=12345, dport=80, flags="PA", seq=1000)
pkt1 = ip/tcp/"GET /evi"
pkt2 = ip/TCP(sport=12345, dport=80, flags="PA", seq=1009)/"l.js HTTP/1.1\r\nHost: test.com\r\n\r\n"

wrpcap("input.pcap", [pkt1, pkt2])
```
img: generate_payload

rodei isso
```python
python3 generate_payload.py 
```
This script **does not send the packets**, it only **generates a .pcap file** containing two TCP packets with a split payload.

img py_payload

input.pcap gerou esses dados

�ò�����s\h�H00E0@��������d09P�P▒ �KGET /evi�s\h�HIIEI@��������d09P�P▒ �l.js HTTP/1.1
Host: test.com


---

## 7. Traffic Replay (This was a key learning point)

### 🔍 My doubt: "How does Suricata actually see this traffic?"

Tive que pesquisar e achar uma maneira de como passar isso pela rede do kali para o suricata entao achei o tcpreplay (Melhore e de mais contexto e explique rapidamente oq é a ferramnta tbm)

So the correct way is to **replay the packets onto the network**.

---


Para mandar o pacote pela rede, precisamos dos seguintes passos 

### Step 1 — Check which interface Kali uses

Run:

```bash
ip route
```

Look for something like:

```
default via 192.168.100.1 dev eth0
```
img: kali_interface

This means `eth0` is your outbound interface.

---

### Step 2 — Send the traffic using tcpreplay

```bash
sudo tcpreplay -i eth0 input.pcap
```

This **injects the crafted packets into the network**, making them observable to Suricata running on pfSense.

If needed, slow it down:

```bash
sudo tcpreplay -i eth1 --pps=1 input.pcap
```

This was an important realization: Suricata doesn’t “magically see” the PCAP unless it’s either replayed (like above) or passed directly with `-r` (which is a different mode).

---

### 🧭 Real-world issue: Scapy-generated pcap initially rejected by tcpreplay

When first attempting to replay the generated traffic using `tcpreplay`, I encountered this fatal error:

```yaml
Fatal Error in get.c:get_l2len_protocol() line 442:
Unable to process unsupported DLT type: Raw IPv4 (0xe4)
```

This revealed that the `.pcap` created by Scapy was missing the Ethernet (Layer 2) header. Tools like `tcpreplay` and Suricata expect full Ethernet frames — not just IP/TCP.

---

### ✅ Fix: explicitly add Ethernet headers in Scapy

To resolve this, I updated the Scapy script to explicitly include an `Ether()` layer:

```python
from scapy.all import Ether, IP, TCP, wrpcap

ether = Ether(src="aa:bb:cc:dd:ee:ff", dst="ff:ee:dd:cc:bb:aa")
ip = IP(dst="192.168.100.1")
tcp1 = TCP(sport=12345, dport=80, flags="PA", seq=1000)
tcp2 = TCP(sport=12345, dport=80, flags="PA", seq=1009)

pkt1 = ether / ip / tcp1 / "GET /evi"
pkt2 = ether / ip / tcp2 / "l.js HTTP/1.1\r\nHost: test.com\r\n\r\n"

wrpcap("input.pcap", [pkt1, pkt2])
```

This generates a valid `.pcap` using Ethernet encapsulation (EN10MB), which is required for proper replay on real interfaces.

---

### 🧪 Replay confirmation

After regenerating the `.pcap`, the replay was successful using:

```shell
tcpreplay -i eth0 input.pcap
```

**Output:**
```yaml
Actual: 2 packets (149 bytes) sent in 0.000116 seconds
Rated: 1284482.7 Bps, 10.27 Mbps, 17241.37 pps
Flows: 1 flows, 8620.68 fps, 2 unique flow packets, 0 unique non-flow packets
Statistics for network device: eth0
Successful packets: 2
Failed packets: 0
Truncated packets: 0
Retried packets (ENOBUFS): 0
Retried packets (EAGAIN): 0
```

---

### 🎯 Takeaway

This reinforced an important insight: engines like Suricata depend on **complete L2 framing** during replay — otherwise, the packets are silently dropped or rejected.

It also reminded me that **low-level details in packet construction matter**, even when simulating traffic.


---

## 8. Observation

### From pfSense:

Access via SSH or GUI and check the `eve.json` logs:

```bash
cat /var/log/suricata/<interface>/eve.json | grep evil.js
```

Check for:

- Alerts triggered
- Presence of `http.uri`
- HTTP parsing context

---

## 9. Expected Results

| Run Context         | Reassembly Enabled | Alert Triggered | URI Detected | HTTP Parsed |
|---------------------|--------------------|------------------|--------------|--------------|
| With Scapy + tcpreplay | ✅ Yes            | ✅ Yes           | ✅ `/evil.js`| ✅ Yes        |
| With reassembly disabled | ❌ No          | ❌ No           | ❌ No        | ❌ No        |

---

## 10. Conclusion

This was my first real-world test validating **TCP reassembly as a requirement for correct detection**.

I initially thought rule matching was simply about string presence, but I learned that engines like Suricata require **stream reassembly** to parse fragmented content.

Also, I learned the difference between:

- Generating packets (`.pcap`)
- Replaying them (`tcpreplay`)
- Feeding them offline (`-r`)

The distinction between seeing traffic “live” vs. “replayed” was crucial.

This experiment grounded my understanding of what it really means for an IDS/IPS to detect traffic — not in theory, but in actual operational mechanics.
                                                                                           