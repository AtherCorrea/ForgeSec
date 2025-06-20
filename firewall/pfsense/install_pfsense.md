# 🧱 Installing pfSense CE

This document covers the installation and initial configuration of the pfSense Community Edition as the firewall for the SOC homelab.

---

## 🔧 Installation Steps

1. **Download ISO**  
   Source: [DSU pfSense Mirror](https://repo.ialab.dsu.edu/pfsense/)
   - Version: `pfSense-CE-2.7.2-RELEASE-amd64.iso`
   - Format: ISO (for CD/DVD boot)

2. **Extraction Issues**  
   Attempting to extract the `.iso.gz` with the Windows native unzip tool resulted in error `0x800070522`.  
   ✅ **Solved by using [7-Zip](https://www.7-zip.org/)** — recommended for handling compressed ISO files safely.

3. **VM Settings (VMware Workstation Pro 17)**  
   - CPU: 2 vCPUs  
   - RAM: 4GB  
   - Disk: 20GB  
   - Network Interfaces:
     - `NAT` (assigned to WAN – internet access)
     - `LAN-01` (isolated lab network)

---

## 🧱 Initial Network Setup

| Interface | Network interface | IP Address        | Purpose               |
|-----------|-------------------|-------------------|---------------------- |
| WAN       | ens33             | DHCP (from NAT)   | External connectivity |
| LAN       | ens37             | 192.168.100.1/24  | Internal SOC network  |

Interfaces were correctly assigned during the pfSense setup wizard. LAN was manually configured with a static IP (`192.168.100.1`) to serve as the default gateway for the internal lab network.

---

## ⚠️ Common Issues Faced

- ❌ **ICMP from Windows Server blocked by default**  
  ✅ Resolved by enabling **ICMPv4 Echo Request** in the Windows Server firewall settings

- ❌ **WAN interface slow to initialize after reboot**  
  ✅ Behavior confirmed to be normal — requires patience on pfSense boot

---

> ✅ pfSense installation and basic connectivity were validated by pinging between pfSense and other hosts.
