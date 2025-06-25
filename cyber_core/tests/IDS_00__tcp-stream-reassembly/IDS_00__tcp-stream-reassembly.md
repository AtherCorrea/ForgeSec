# Test Case – TCP Stream Reassembly and Fragmented Payload Detection

## 1. Goal

To validate the impact of TCP stream reassembly on detecting fragmented payloads — especially when traffic is deliberately split to evade content-based detection mechanisms.

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
  - Python 3.x with Scapy → `pip3 install scapy`
  - `tcpreplay` → install with `sudo apt install tcpreplay`
- **On pfSense:**
  - Suricata must be running on the **LAN interface**
  - Only the custom rule `/evil.js` should be active (to eliminate noise)

---

## 5. Payload Creation

### Step 1 — Create the test folder

```bash
mkdir -p ~/forgesec/cyber_core/tests/00_tcp-stream-reassembly/
cd ~/forgesec/cyber_core/tests/00_tcp-stream-reassembly/
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

This script **does not send the packets**, it only **generates a .pcap file** containing two TCP packets with a split payload.

This was something I initially misunderstood — I thought `generate_payload.py` would send traffic directly, but it doesn’t.

### Step 3 — Confirm the file

```bash
ls -lh input.pcap
```

---

## 6. Rule Setup

### Step 1 — Create detection rule

```bash
nano rules.rules
```

Add:

```
alert http any any -> any any (msg:"Detected /evil.js"; content:"/evil.js"; sid:1000001;)
```

This rule detects any occurrence of `/evil.js` in HTTP traffic — **but it only works** if the content is visible after reassembly.

---

## 7. Traffic Replay (This was a key learning point)

### 🔍 My doubt: "How does Suricata actually see this traffic?"

Initially I assumed generating the PCAP was enough. But I realized that unless Suricata actually **observes the packets passing through the wire**, it can’t apply the detection logic in real time.

So the correct way is to **replay the packets onto the network**.

---

### Step 1 — Check which interface Kali uses

Run:

```bash
ip route
```

Look for something like:

```
default via 192.168.100.1 dev eth1
```

This means `eth1` is your outbound interface.

---

### Step 2 — Send the traffic using tcpreplay

```bash
sudo tcpreplay -i eth1 input.pcap
```

This **injects the crafted packets into the network**, making them observable to Suricata running on pfSense.

If needed, slow it down:

```bash
sudo tcpreplay -i eth1 --pps=1 input.pcap
```

This was an important realization: Suricata doesn’t “magically see” the PCAP unless it’s either replayed (like above) or passed directly with `-r` (which is a different mode).

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
                                                                                           