# 🔥 Firewalls & Gateways – SOC Homelab

This folder contains configuration files, documentation, and tests related to **network perimeter defense** in the SOC Homelab.

---

## 🛡️ Purpose

Firewalls act as the first layer of defense, filtering traffic and segmenting networks. They also enable **network address translation (NAT)** and policy-based control over interfaces.

---

## 🧱 Components So Far

| Tool       | Role                            |
|------------|----------------------------------|
| `pfSense`  | Main gateway & traffic shaper    |

🔗 pfSense config files: [`firewall/pfsense`](./pfsense)

---

## 📌 Folder Structure

- `pfsense/` → Contains:
  - Backup configs
  - Setup documentation
  - Test cases and logs

> As the project evolves, this section may include other gateway or firewall technologies (e.g., OPNsense, VyOS, nftables).
