# Created and maintained by Ather Correa

Security researcher & homelab architect focused on realistic SOC simulation, blue team tooling and adversary traffic generation.

**LinkedIn:** linkedin.com/in/athercorrea/

# Ignitor

**Ignitor** is a modular security testing framework designed to simulate malicious and benign traffic in order to trigger, test, and validate detection mechanisms within Security Operations Centers (SOCs), firewalls, SIEMs, and EDRs.

This tool is ideal for blue teams, SOC analysts, threat hunters, and cybersecurity researchers who want to stress and validate defensive environments with realistic traffic patterns.

---

## 🔥 Features

- Simulated access to known malicious IPs, URLs and domains
- Trigger-based modules for web filtering, application control, and SIEM detection
- Legitimate traffic simulation to test false positives and baseline noise
- Modular and extensible CLI interface with `click`
- Easy to use in homelabs or production-like test environments

---

### 📁 Project Structure (planned)

ignitor/
├── ignitor.py           # Main CLI script
├── modules/             # Submodules for each functionality (IPRep, VXVault, etc.)
├── requirements.txt     # Dependencies
├── LICENSE              # MIT License
└── README.md            # You are here

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.8 or higher
- Internet access for threat feed modules

### 📦 Installation

```bash
git clone https://github.com/seunome/ignitor.git
cd ignitor
pip install -r requirements.txt
```

### 🔧 Running the tool

```bash
python3 ignitor.py --help
python3 ignitor.py example
```
