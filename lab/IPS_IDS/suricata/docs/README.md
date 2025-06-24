# 📘 Suricata Documentation – Setup & Configuration

This folder contains practical documentation on the installation and configuration of **Suricata IDS** within the pfSense firewall, as part of the SOC Homelab environment.

Suricata is responsible for analyzing traffic on the internal LAN and generating alerts based on rule sets.

---

## 📚 Contents

- `install_suricata.md` – Step-by-step installation guide using the pfSense Package Manager
- `test/` – Folder linking to detection experiments and test case descriptions
- `img/` – Folder containing images used throughout the documentation

---

## 📍 Purpose

This documentation helps track how Suricata was deployed and configured in the lab. It complements the detection tests by recording:

- Which interfaces were monitored
- Which rules were enabled
- How logs and alerts behaved in each scenario

It also serves as a reference for future adjustments, integrations, or performance tuning.

---

> 📄 For deep theoretical content on IDS/IPS engines and how they work internally, refer to the learning path under:  
> [`docs/learning/IPS_IDS`](../../../../docs/learning/IPS_IDS)
