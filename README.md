# 🛡️ Ather SOC Homelab

Ather SOC Homelab is a fully documented, realistic simulation environment designed for in-depth learning of cybersecurity operations. It was built from scratch to explore how modern SOC components operate in real-world conditions — including malicious traffic detection, network defense, and event correlation.

> This is not just a demo lab — it's a real, evolving project focused on **understanding cybersecurity with depth**. Every tool, test, and problem is documented with the mindset of a professional analyst and engineer. This repository is part of my public portfolio to show both **technical capability** and **professional documentation standards**.

---

## 🎯 Objectives

- Build a realistic, modular SOC homelab using virtualized infrastructure
- Learn cybersecurity operations with practical, real-world use cases
- Understand network behavior, system monitoring, log analysis, and threat detection
- Create a custom offensive testing tool — [IGNITE](../ignite)
- Showcase high-quality documentation and structured testing

---

## 🧱 Lab Overview

The lab simulates an enterprise-like network using VMware Workstation Pro 17. It uses isolated NAT and LAN segments to ensure realistic traffic flow and separation of responsibilities.

> For full architecture and network details, refer to [`lab/topology.md`](./lab/topology.md).

---

## 🧪 Tests and Analysis

Each test case in this repository is structured to provide:

- The attack vector used (with exact commands)
- The network context and target
- The detection output (from IDS, firewall, or SIEM)
- Screenshots, raw logs, and observations

📂 Example structure:

```
/ids/suricata/tests/test-01_nmap-scan/
├── description.md
├── eve.json
├── screenshot.png
└── rules-activated.txt
```

All logs are versioned and cleaned before each test to ensure traceability and reproducibility.

---

## 🧩 Tools & Components

The environment is built using multiple virtual machines, each fulfilling a realistic role in a corporate network.

> Configuration details are provided per component in their respective folders, such as [`/firewall/pfsense`](./firewall/pfsense) and [`/ids/suricata`](./ids/suricata).

---

## 🧠 Why This Project?

The mission behind this project goes beyond simulating alerts — it's about building a deep understanding of cybersecurity as a discipline.

From traffic inspection and protocol behavior, to rule-based detection and event correlation, this lab is a foundation to study how everything connects inside a real SOC. This includes:

- Core concepts of detection, logging, and alerting
- Traffic behavior across firewall and IDS/IPS layers
- How tools integrate and correlate data in a SIEM
- Troubleshooting real-world system and network challenges

> You’ll find examples of these challenges — like ICMP being blocked by a Windows firewall or missing rule activations — fully documented in their appropriate sections (e.g., [`learning.md`](./docs/learning.md)).

---

## 📚 Documentation

You’ll find detailed notes and configs structured by area:

- [`docs/roadmap.md`](./docs/roadmap.md) – project plan and progress
- [`docs/learning.md`](./docs/learning.md) – problems faced, lessons learned
- [`lab/topology.md`](./lab/topology.md) – network structure and diagram
- [`firewall/pfsense/config`](./firewall/pfsense/config) – pfSense configuration backups
- [`ids/suricata/tests`](./ids/suricata/tests) – detection tests and results

> 📚 **This is real documentation from a real lab**, not placeholder notes. The goal is to impress not with flashy visuals, but with structured, transparent, and replicable research.

---

## 🤝 Connect

If you’re a recruiter, SOC analyst, or cybersecurity enthusiast — feel free to connect and follow this journey:

- 🔗 [LinkedIn – Ather Correa](https://www.linkedin.com/in/athercorrea/)
- 📬 GitHub: [github.com/AtherCorrea](https://github.com/AtherCorrea)

> ⭐ If this project inspired you, feel free to star it and share.
