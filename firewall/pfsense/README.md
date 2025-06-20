# 🔥 pfSense – Firewall Configuration

This directory holds all configuration files, behavior tests, and documentation related to **pfSense**, the primary firewall in the SOC lab. pfSense is used to enforce network segmentation, control traffic between interfaces, and serve as the integration point for IDS/IPS functionality (Suricata).

By deploying pfSense in the lab, we simulate a real corporate perimeter and internal firewall setup.

---

## 📦 Contents

- [`config/`](./config/) – Exported configuration files and interface setup
- [`tests/`](./tests/) – Connection tests, ICMP rules, NAT behavior, and more

---

## 🎯 Objective

- Deploy a fully functional virtual firewall in the lab environment
- Control and isolate traffic using NAT and interface rules
- Provide a stable base for IDS/IPS integration and SIEM data ingestion
- Study how firewalls behave under scan, stress, and misconfiguration

---

## 🧪 Example Test Case

```
test-icmp-blocked/
├── description.md         # Problem and solution
├── screenshot.png         # Rule configuration
└── notes.md               # Observations and impact
```

Each test is tracked to show real network behavior and its impact on visibility and control.
