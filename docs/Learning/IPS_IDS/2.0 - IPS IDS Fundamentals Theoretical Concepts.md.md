# 🧠 IDS/IPS Fundamentals – Theoretical Concepts

This section introduces the core concepts behind Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS). Understanding these foundations is critical before diving into lab testing and signature analysis.

---

## 📌 What is an IDS?

An **Intrusion Detection System** is a security solution that monitors network or host activity for signs of malicious behavior. It **detects**, but does **not block** by default.

🔗 [IDS Explained – GeeksforGeeks](https://www.geeksforgeeks.org/intrusion-detection-system-ids/)

### Key Capabilities

- Analyzes traffic using predefined rules or anomaly detection
- Raises alerts for suspicious or known attack patterns
- Logs events for SOC analysis or SIEM correlation

### Types

- **NIDS** – Network-based IDS: Monitors traffic on the entire network
- **HIDS** – Host-based IDS: Monitors a specific host or endpoint
- **PIDS** – Protocol-based IDS: Analyzes protocol-specific traffic (e.g., HTTP, FTP)
- **Application Protocol-based IDS** – Monitors application-specific traffic at the application layer

---

## 📌 What is an IPS?

An **Intrusion Prevention System** builds on IDS capabilities but **actively blocks** malicious activity in real time.

🔗 [What is IPS – Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-an-intrusion-prevention-system-ips)

### Key Capabilities

- Detects threats and takes automatic action (drop, reject, reset)
- Works inline between networks or endpoints
- Ideal for high-security environments where response time is critical

> In pfSense + Suricata, enabling IPS mode allows packet rejection instead of passive alerting.

---

## 🔍 IDS vs IPS vs Firewalls

| Feature           | IDS                          | IPS                          | Firewall                    |
|------------------|------------------------------|------------------------------|-----------------------------|
| Position         | Out-of-band                  | Inline                       | Inline                      |
| Action           | Detect and alert             | Detect, alert, and block     | Allow/deny based on rules   |
| Visibility       | Application and protocol layer| Same as IDS                  | Mostly network/port layer   |
| Signature usage  | Yes                          | Yes                          | Yes (simpler rules)         |
| Stateful analysis| Sometimes                    | Yes                          | Yes                         |

🔗 [IDS vs IPS – Comparitech](https://www.comparitech.com/net-admin/ids-vs-ips/)

---

## ⚙️ Detection Modes

- **Signature-based**  
  Matches known patterns (e.g., payloads, headers, user-agents).  
  ✅ High precision  
  ❌ Misses unknown attacks  
  🔗 [Signature-based detection explained – Corelight](https://corelight.com/resources/glossary/signature-based-detection)

- **Anomaly-based**  
  Builds a baseline of “normal” behavior and flags deviations.  
  ✅ Can detect zero-days  
  ❌ High false positive rate if not tuned  
  🔗 [Anomaly Detection in Cybersecurity – IBM](https://www.ibm.com/topics/anomaly-detection)

- **Hybrid-based**  
  Combines both signature and anomaly-based approaches for improved detection range and accuracy.  
  Many modern systems, including Suricata, support hybrid approaches.

🔗 [Suricata Overview – OISF](https://suricata.io/about/)

---

## 🎛️ Deployment Modes

- **Passive (IDS Mode)**  
  Monitors traffic from a mirror port or SPAN. Ideal for low-risk learning environments.

- **Inline (IPS Mode)**  
  Intercepts and processes packets before they reach the destination. Can block in real time.

> In our lab, we start with IDS mode to safely observe behavior and learn before enabling active prevention.

🔗 [Suricata IDS vs IPS Modes – Official Docs](https://docs.suricata.io/en/latest/configuration/suricata-yaml.html#running-mode)

---

## 🧠 Why This Matters

Intrusion Detection and Prevention Systems (IDS/IPS) are a critical component of any layered security architecture. They offer visibility and control over network traffic beyond what traditional firewalls provide.

### Key Benefits

- 📈 Analyze logs with deeper context to support incident response
- 🧠 Improve detection accuracy by identifying false positives and tuning rules
- 🔐 Strengthen network defense through real-time alerts and/or traffic blocking
- 🛠️ Build better detection pipelines and integrate with SIEM platforms
- 🎯 Support advanced strategies like threat hunting, forensics, and blue team operations

> IDS/IPS solutions act as your **network's security intelligence layer**, helping identify and mitigate threats before they cause damage.

### Further Reading

- 🔗 [Why Intrusion Detection and Prevention Systems are Still Important – HBS](https://www.hbs.net/blog/why-intrusion-detection-and-prevention-systems-are-still-important)  
- 🔗 [IDS & IPS Remain Important Even as Other Tools Add IDPS Features – eSecurity Planet](https://www.esecurityplanet.com/networks/ids-vs-ips/)

---

## 🧩 Next Step

Move on to [Suricata Deep Dive](./suricata_architecture.md) to understand how Suricata operates internally and how traffic is analyzed at the packet level.
