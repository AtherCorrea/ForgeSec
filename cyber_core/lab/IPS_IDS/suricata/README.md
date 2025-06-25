# 🛡️ Suricata IDS – Configuration & Testing

This folder contains documentation, configurations, and structured tests for **Suricata**, our main IDS/IPS engine deployed via pfSense in the Ather SOC Homelab.

Suricata is used to detect malicious behavior, generate alerts, and help us understand how packet-based threat detection works in a real-world setup.

---

## 📦 Folder Structure

| Folder        | Description                                                  |
|---------------|--------------------------------------------------------------|
| `docs/`       | Step-by-step installation guide and deep-dive architecture   |
| `tests/`      | Hands-on detection tests with raw logs and screenshots       |

---

## 🎯 Objective

- Deploy and configure Suricata using pfSense
- Activate and analyze detection rules (ET Open, custom)
- Observe how alerts are triggered and logged (`eve.json`, `fast.log`)
- Simulate realistic attacks (e.g., Nmap, scanning, etc.)
- Serve as a base for future SIEM correlation and automation

---

## 🧪 Example Test Case Format

Each test includes a reproducible structure like:

test-01_nmap-scan/
├── description.md # Test explanation and attack goal
├── eve.json # Suricata alert logs
├── screenshot.png # pfSense GUI screenshot of alert
└── rules-activated.txt # Rules that were active during test

> Logs are reset and versioned before each test to maintain reproducibility and avoid noise between tests.

---

## 📚 Related Learning Material

This component is part of the broader IDS/IPS study track.

📄 Reference: [`2.0 - IPS-IDS Fundamentals – Theoretical Concepts`](../../../docs/Learning/IPS_IDS/2.0%20-%20IPS%20IDS%20Fundamentals%20Theoretical%20Concepts.md.md)  
📄 Reference: [`2.1 - How IDS/IPS Engines Work`](../../../docs/Learning/IPS_IDS/2.1%20-%20How%20IDS_IPS%20Engines%20Work.md)
