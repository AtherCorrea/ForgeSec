# Ignitor

**Ignitor** is a security testing framework designed to simulate threat traffic and trigger detection mechanisms in SOC environments.

## Features
- Simulate malicious and benign traffic
- Trigger firewall/SIEM/EDR alerts
- Run tests with customizable source IPs
- CLI-based, modular, ideal for homelabs and blue teams

## Getting Started

```bash
git clone https://github.com/AtherCorrea/ignitor.git
cd ignitor
pip install -r requirements.txt
python3 ignitor.py --help
