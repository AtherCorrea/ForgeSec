# 🛡️ Suricata IDS – Configuration & Testing

This folder contains the configuration and structured detection tests for **Suricata**, a powerful open-source IDS (Intrusion Detection System). Suricata is deployed on the pfSense firewall to monitor traffic on the internal SOC LAN segment.

It plays a critical role in identifying suspicious or malicious network activity and is key to understanding how rule-based detection works in real environments.

---

## 📦 Contents

- [`docs/`](./docs/) – Installation guide and configuration steps for Suricata on pfSense
- [`tests/`](./tests/) – Hands-on tests with logs, screenshots, and triggered alerts

---

## 🎯 Objective

- Understand the fundamentals of IDS operation in a controlled network
- Activate and test detection rules under different attack conditions
- Learn how alerts are triggered, logged, and interpreted
- Simulate traffic that mirrors real-world threats and verify Suricata's behavior

---

## 🧪 Example Test Case

Each test includes everything needed to trace the detection:

```
test-01_nmap-scan/
├── description.md         # Test description and goal
├── eve.json               # Raw Suricata logs
├── screenshot.png         # GUI view of alert
└── rules-activated.txt    # List of rules active for the test
```

Logs are reset and versioned per test to ensure reproducibility and clarity for future comparison.

---
