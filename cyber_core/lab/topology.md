# Network Topology – ForgeSec

The lab environment is designed with a focus on controlled isolation, full observability, and realistic simulation of a corporate network.

---

## 🌐 Virtual Network Architecture

The lab uses a dual-network setup in VMware Workstation:

- **NAT**: Provides internet access (VMnet8)
- **LAN-01**: Isolated internal network (VMnet2), used for simulating real internal host communication

These networks are configured using VMware's Virtual Network Editor, allowing:

- Outbound traffic through NAT
- Full isolation between the LAN segment and the host machine
- All inter-segment routing is handled by pfSense

---

## 📦 Current Virtual Machines

| VM Name         | OS Version          | IP Address       | Network Adapters     | Role/Description                           |
|-----------------|---------------------|------------------|----------------------|--------------------------------------------|
| **pfSense**     | pfSense CE / Plus   | 192.168.100.1    | LAN-01, WAN (NAT)    | Main gateway and IDS/IPS (Suricata running in IDS mode on both LAN and WAN interfaces) |
| **Kali Linux**  | Kali Rolling        | 192.168.100.20   | NAT                  | Attacker simulation. Generates malicious traffic (Scapy, Nmap, Ignaitor). Reaches LAN via pfSense routing |
| **Debian Server** | Debian 12         | 192.168.100.30   | LAN-01               | Future SIEM (Wazuh/ELK). Log and correlation server |
| **Windows Server** | Server 2022      | 192.168.100.10   | LAN-01               | Domain Controller (Active Directory, DNS, DHCP) |

> Note: Although Kali is only connected to NAT, it can reach LAN-01 hosts through routing and NAT rules configured in pfSense. This enables controlled bidirectional communication for simulating both internal and external attacks.

---

## 🧠 Network Design

- All internal traffic flows through the **LAN-01** network
- **pfSense** acts as **router, firewall, and IDS/IPS**, routing traffic between NAT (WAN) and LAN interfaces
- Suricata runs in **passive IDS mode** on both WAN and LAN interfaces
- Some VMs (like Kali) have NAT enabled only for external access, but all attack traffic is routed through pfSense

---

## 🖼️ Diagram

(Coming soon – include visual topology diagram here once created.)

---

This environment is purpose-built to simulate a real SOC, with full capability to generate, intercept, and analyze malicious traffic under controlled conditions.
