# 💻 Virtual Machines – SOC Homelab

This folder documents the setup and configuration of all virtual machines used in the Ather SOC Homelab environment. Each VM represents a key component in the simulated enterprise infrastructure.

---

## 🧩 Purpose

The VMs serve different roles in the lab — such as attack simulation, domain control, SIEM hosting, and end-user behavior — allowing realistic interaction across the network.

---

## 🖥️ Machines Included

| VM Name             | Purpose                              | OS                    |
|---------------------|---------------------------------------|------------------------|
| `windows_server.md` | Domain Controller, event generator    | Windows Server 2019    |
| `debian_server.md`  | SIEM backend and log collector        | Debian 11              |
| `metasploitable2.md`| Vulnerable target for testing         | Metasploitable 2       |
| `kali.md`           | Offensive attacker box (red team)     | Kali Linux             |

---

## 📌 Notes

- Each file contains: VM specs, installation method, initial config, and network integration.
- All VMs are managed through **VMware Workstation Pro 17**.
- Network adapters are manually mapped to match the lab’s isolated subnets.

> This section will evolve as we integrate more systems and expand test coverage.
