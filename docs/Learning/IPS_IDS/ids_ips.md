# 🧠 2.1 - How IDS/IPS Engines Work

This document explains how Intrusion Detection and Prevention Systems (IDS/IPS) operate internally — covering traffic inspection architecture, detection pipelines, and how systems like Suricata process and react to packets in real time.

> While Suricata is our main lab tool, these concepts apply broadly across modern IDS/IPS engines.

---

## 🧩 IDS/IPS Architecture – Step-by-Step

Below is a structured breakdown of the internal components of an IDS/IPS engine, arranged logically by data flow.

---

### 1. 📥 Packet Capture and Ingestion

- Captures raw packets using interfaces like `libpcap`, `AF_PACKET`, `Netmap`, `DPDK`
- Supports passive (mirror port) or inline (bridge) modes
- Optional BPF filters to reduce input noise
- Interfaces can be bonded or tied to specific VLANs

---

### 📎 References – Packet Capture & Ingestion

| 🔍 | Related To     | Title                                                                                  | Link                                                                 |
|----|----------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 📄 | libpcap        | Stanford – The Sniffer's Guide to Raw Traffic                                          | [Link](https://yuba.stanford.edu/~casado/pcap/section1.html)        |
| 📄 | BPF            | IBM – Berkeley Packet Filters                                                          | [Link](https://www.ibm.com/docs/en/qsip/7.4?topic=queries-berkeley-packet-filters) |
| 📄 | AF_PACKET      | Linux Kernel – Packet MMAP & AF_PACKET                                                 | [Link](https://docs.kernel.org/networking/packet_mmap.html)         |
| 📄 | DPDK           | DPDK – AF_PACKET Poll Mode Driver                                                      | [Link](https://doc.dpdk.org/guides/nics/af_packet.html)             |
| 📚 | libpcap        | Medium – Libpcap usage in C                                                            | [Link](https://bettercybersec.com/snort-packet-capture-with-libpcap/) |
| 📚 | Linux Kernel   | Medium – Capturing millions of packets/s with Linux only                               | [Link](https://medium.com/@pavel.odintsov/capturing-packets-in-linux-at-a-speed-of-millions-of-packets-per-second-without-using-third-party-ef782fe8959d) |
| 📚 | AF_PACKET      | elf11 Blog – AF_PACKET deep dive                                                       | [Link](https://elf11.github.io/)                                    |
| 🎥 | BPF            | YouTube – Introduction to BPF (CodiLime)                                               | [Link](https://www.youtube.com/watch?v=DiYVJ1sE9b0)                  |
| 🎥 | DPDK           | YouTube – DPDK Packet Capture                                                          | [Link](https://www.youtube.com/watch?v=CQ3uuAeLk7I)                  |
| 🧵 | AF_PACKET      | Elastic Discuss – AF_PACKET vs libpcap performance                                     | [Link](https://discuss.elastic.co/t/performance-difference-between-af-packet-libpcap/69766) |
| 🧵 | AF_PACKET      | Suricata Forum – AF_PACKET bridge IPS mode issues                                      | [Link](https://forum.suricata.io/t/af-packet-ips-mode-not-copy-tcp-ack/3782) |
| 🧵 | AF_PACKET      | Suricata Forum – Configuration & performance issues                                    | [Link](https://forum.suricata.io/t/suricata-ids-does-not-work-in-af-packet-ips-mode/3996) |
| 💡 | AF_PACKET      | NetDevConf – AF_PACKET v4 & PACKET_ZEROCOPY                                            | [Link](https://netdevconf.info/)                                    |
| 📘 | BPF            | Wikipedia – Berkeley Packet Filter                                                     | [Link](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter)        |
| 📘 | eBPF           | Wikipedia – eBPF                                                                       | [Link](https://en.wikipedia.org/wiki/EBPF)                          |

🔗 [Suricata Packet Capture Docs](https://docs.suricata.io/en/latest/performance/packet-capture.html)

---

### 2. 🔄 Packet Decoding and Normalization

- Extracts Ethernet, IP, TCP/UDP, and application-layer protocols (e.g., HTTP, TLS, DNS)
- Reassembles fragmented packets
- Handles TCP stream reconstruction
- Prevents evasion by normalizing weird/broken traffic

---

### 3. 🔗 Flow and Session Tracking

- Tracks bidirectional connections (5-tuple: src IP, dst IP, src port, dst port, protocol)
- Enables context-aware rule evaluation
- Maintains state for protocols like TCP and UDP
- Critical for advanced detections (e.g., long sessions, slow attacks)

---

### 4. 🧠 Detection Pipeline (Rule Matching)

- Evaluates packets and flows against loaded rules
- Rule structure includes:
  - `msg`, `sid`, `classtype`, `priority`
  - Match conditions: `content`, `http_uri`, `pcre`, `flowbits`, etc.
  - Rule actions: `alert`, `drop`, `reject`
- Optimized matching engine using keyword trees

🔗 [Suricata Rule Language](https://docs.suricata.io/en/latest/rules/intro.html)

---

### 5. 🧵 Multithreading and Performance Model

- Threading modes: `autofp`, `workers`, `pcap` modes
- CPU core pinning and flow hashing
- One thread per packet stream or capture interface
- Tuning parameters:
  - `detect-thread-ratio`
  - Flow timeouts and buffer sizes

🔗 [Performance Tuning Guide – Suricata Docs](https://docs.suricata.io/en/latest/performance/intro.html)

---

### 6. 📤 Output Modules & Logging

- Formats:
  - `eve.json`: structured JSON event log
  - `fast.log`: flat text alerts
  - `stats.log`: performance metrics
- Fields logged:
  - Rule SID, timestamp, flow ID, protocol, packet metadata
- Logs are consumed by SIEMs or dashboards

🔗 [EVE JSON Output – Suricata Docs](https://docs.suricata.io/en/latest/output/eve/eve-json-output.html)

---

### 7. ⚙️ IDS vs IPS Modes

| Mode | Description | Use Case |
| ---- | ----------- | -------- |
|      |             |          |

| **Passive** | Observes traffic via mirror/SPAN port    | Safe analysis and monitoring     |
| ----------- | ---------------------------------------- | -------------------------------- |
| **Inline**  | Acts as a bridge; can drop/block packets | Real-time prevention and control |

> We begin with Passive mode for learning and safety. IPS mode may be tested in isolated setups later.

---

### 8. 🧪 Real Packet Journey Example

> Follow a packet from capture to alert:

```text
[ Ethernet frame received ]
        ↓
[ Packet decoded (L2–L7) ]
        ↓
[ Reassembled into TCP/UDP flow ]
        ↓
[ Preprocessors enrich metadata ]
        ↓
[ Detection engine evaluates rules ]
        ↓
[ Alert triggered → Output module logs event ]
```

This mental model helps us debug alerts and rule behavior.

---

## 🛠️ Practical Lab Plan: What We'll Test

We will implement hands-on tests to reinforce this understanding:

1. **Verify capture interface behavior**

   - Use `tcpdump` and Suricata side-by-side to confirm packet flow

2. **Observe decoding and flow creation**

   - Monitor Suricata stats to see flows being created per connection

3. **Trigger known rule-based detections**

   - Use Nmap, Nikto, and simple payloads
   - Trace alert path in `eve.json`

4. **Analyze multithread behavior**

   - Use `htop`, `suricata.log`, and `stats.log` during load

5. **Switch from IDS to IPS mode** *(optional phase)*

   - Enable inline mode and test packet dropping

All findings will be documented under `lab/IPS_IDS/suricata/tests/`

---

## ✅ Summary

Understanding the internal workflow of IDS/IPS engines helps us:

- Write more effective detection rules
- Optimize Suricata performance
- Troubleshoot missed or noisy alerts
- Build confidence in alerts generated by the system

📄 Next: [`2.2 - IDS Rule Anatomy and Behavior`](./2.2%20-%20IDS%20Rule%20Anatomy%20and%20Behavior.md)
