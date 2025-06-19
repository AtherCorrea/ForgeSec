#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ignitor - Simulated Threat Traffic & SOC Trigger Framework

Ignitor is a modular framework designed to simulate security events, trigger detection mechanisms,
and evaluate the performance of Security Operations Centers (SOCs). It enables the generation of
malicious and benign traffic, IP/domain IOCs, application-level triggers, and more — ideal for
blue team testing, SIEM rule validation, and homelab defense validation.
"""

import click
import requests
from urllib3.exceptions import InsecureRequestWarning
import platform
import socket
import random

# Optional - will be used in future steps
# from requests_toolbelt.adapters.source import SourceAddressAdapter
# from selenium import webdriver

# Disable HTTPS warnings (we'll simulate malicious access)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__version__ = "0.1-dev"

# Console colors (if supported)
W, R, G, O, B, P, C, GR = '\033[0m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'

if platform.system() == "Windows":
    W = R = G = O = B = P = C = GR = ''  # No colors on Windows by default

def banner():
    print(r"""
     ___           _       _             
    |_ _|_ __  ___| |_ ___| |_ _ __ ___  
     | || '_ \/ __| __/ _ \ __| '__/ _ \ 
     | || | | \__ \ ||  __/ |_| | | (_) |
    |___|_| |_|___/\__\___|\__|_|  \___/ 
       Security Operations Testing Tool
    """)
    print("Ignitor - Simulated Threat Traffic & SOC Trigger Framework")
    print(f"Author: Ather Correa | Version: {__version__}\n")


@click.group(chain=True)
def cli():
    banner()
    # Test network availability
    try:
        requests.get("https://www.google.com", timeout=5, verify=False)
        print(G + "[+] " + W + "Network connection is OK")
    except:
        print(R + "[!] " + W + "No internet connection detected.")
        exit(1)


@cli.command()
def example():
    """Example placeholder command"""
    print(B + "[*] " + W + "This is a placeholder for future functionality.")


if __name__ == "__main__":
    cli()
