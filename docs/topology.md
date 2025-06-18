# Network Topology – Ather SOC Homelab

The lab uses a dual-network architecture in VMware:

- A **NAT network** for internet access
- A **LAN-only network** for internal lab communication

These networks are configured using VMware's Virtual Network Editor:

- **NAT**: Provides outbound internet access
- **LAN-01**: Isolated lab communication (no host access)

---

## 📦 Current Virtual Machines

| VM Name         | OS Version          | Network Adapters                        | Role/Description                         |
|-----------------|---------------------|-----------------------------------------|------------------------------------------|
| Kali Linux      | Kali Rolling        | LAN-01, NAT   | Attacker simulation: Nmap, Hydra, FIT++  |
| Debian Server   | Debian 12           | LAN-01, NAT                            | Future SIEM server (Wazuh/ELK)           |
| Windows Server  | Windows Server 2022 | LAN-01, NAT                            | Domain Controller (AD, DNS, DHCP)        |

> ⚠️ pfSense not installed yet. Will act as a firewall/IDS with dual interface (NAT/WAN + LAN)

---

## 🧠 Network Design Plan

- All internal traffic flows through the **LAN-01** network
- **pfSense** will act as gateway/firewall between NAT and LAN
- No communication from LAN to host machine ensures full isolation

## 📍 Next Steps

- Install pfSense with two interfaces
- Assign static IPs (or enable DHCP via pfSense)
- Begin configuring Windows AD, SIEM stack, and attack testing

## 🖼️ Diagram

(Coming soon – include visual topology here once created.)
