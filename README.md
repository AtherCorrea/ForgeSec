# 🛡️ Ather SOC Homelab

Ather SOC Homelab is a fully documented, realistic simulation environment designed to deeply understand how modern Security Operations Centers (SOCs) work. This lab includes virtualized firewalls, IDS/IPS, offensive testing, and log analysis everything built from scratch with real tools, real traffic, and real documentation.

> This isn’t just a demo lab it's a **living, technical portfolio** focused on depth, clarity, and professional-grade research. Each component is analyzed and documented as if in a real-world enterprise SOC.

---

## 🌟 Objectives

- Build a modular, enterprise-like SOC homelab using virtual machines and segmented networks
- Learn cybersecurity operations through hands-on simulation and attack emulation
- Understand how logs, packets, and events interact across firewall, IDS/IPS, and SIEM layers
- Create a custom offensive testing tool [`IGNITE`](./ignite)
- Showcase detailed, technical documentation as part of a public portfolio

---

## 🧱 Lab Overview

The lab emulates a corporate network using VMware Workstation Pro 17, with distinct NAT and LAN segments for realism. Components include:

- Windows Server with Active Directory
- pfSense firewall
- Suricata IDS/IPS
- Kali Linux (offensive)
- Metasploitable2 (vulnerable target)
- Debian-based syslog/SIEM servers

> 📄 For full architecture details: [`lab/topology.md`](./lab/topology.md)

---

## 🧪 Tests and Detection Analysis

All security tests follow a repeatable structure with:

- Attack method and exact steps used
- Traffic context and test scope
- Alert/log output (e.g., Suricata or pfSense)
- Screenshots and raw log files

📂 Example:

```
lab/IPS_IDS/suricata/tests/01_suricata_test_nmap-scan/
├── description.md
├── eve.json
├── screenshot.png
└── rules-activated.txt
```

All logs are cleared before testing to ensure traceability and reproducibility.

---

## 🧹 Structure & Components

The repository is divided into logical areas of a SOC environment:

- [`lab/vms`](./lab/vms) – Setup notes and roles of each virtual machine
- [`lab/firewall`](./lab/firewall) – Firewall deployment and configuration
- [`lab/IPS_IDS`](./lab/IPS_IDS) – IDS/IPS systems, detection rules, and testing
- [`ignite`](./ignite) – Custom offensive tool designed for traffic simulation
- [`docs`](./docs) – Learning paths, theory, research, and structured analysis

> Each section has its own `README.md` for navigation and context.

---

## 📚 Learning & Cybersecurity Insights

This project focuses on **understanding cybersecurity as a discipline**, not just on using tools. Topics include:

- Traffic analysis and detection logic in IDS/IPS
- Firewall behavior, filtering, and state tracking
- Rule tuning, signature logic, and alert triage
- SIEM data correlation from multiple sources
- Integration of AI for log parsing and detection support

🧠 Key learning modules:

- [`docs/learning/IPS_IDS/1.0%20-%20Roadmap_IDS-IPS%20Mastery%20Path.md`](./docs/learning/IPS_IDS/1.0%20-%20Roadmap_IDS-IPS%20Mastery%20Path.md)
- [`docs/learning/IPS_IDS/2.0%20-%20IPS-IDS%20Fundamentals%20–%20Theoretical%20Concepts.md`](./docs/learning/IPS_IDS/2.0%20-%20IPS-IDS%20Fundamentals%20%E2%80%93%20Theoretical%20Concepts.md)
- [`docs/learning/IPS_IDS/2.1%20-%20How%20IDS-IPS%20Engines%20Work.md`](./docs/learning/IPS_IDS/2.1%20-%20How%20IDS-IPS%20Engines%20Work.md)

---

## 🚧 Project Status & Future Additions

This lab is under active construction and constantly evolving. Planned enhancements include:

- SIEM integration with Wazuh or Splunk
- Certificate management and secure communication
- Advanced Suricata rule development and classification
- Evasion detection and performance benchmarking
- Extended attack simulation scenarios
- AI modules for log analysis, rule generation, and alert triage

---

## 🤝 Connect

If you're a recruiter, SOC analyst, or cybersecurity enthusiast:

- 🔗 [LinkedIn – Ather Correa](https://www.linkedin.com/in/athercorrea/)
- 📬 GitHub: [github.com/AtherCorrea](https://github.com/AtherCorrea)

> ⭐ Star this repo if you found it inspiring or useful — and feel free to share!
