# 🧪 IDS/IPS Detection Tests

This folder contains test scenarios performed on the IDS/IPS components in the lab — currently focused on Suricata.

Each folder represents a specific attack simulation or traffic test case. It includes:

- A written description of the attack or scan
- Exact tools and commands used
- Activated Suricata rules
- Resulting logs (`eve.json`, screenshots, alert messages)

---

## 🗂️ Folder Structure Example

test-01_nmap-scan/
├── description.md
├── eve.json
├── screenshot.png
└── rules-activated.txt

---

## 🧩 Purpose

- Validate detection rules under controlled attack conditions
- Study how each test is interpreted by the IDS
- Understand alerting behavior and log outputs

> Logs are cleaned and versioned for traceability across each test.
