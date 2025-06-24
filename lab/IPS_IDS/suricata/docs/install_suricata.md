# 🛡️ Installing Suricata on pfSense

Suricata was installed directly as a pfSense package to act as IDS/IPS on the WAN interface.

---

## 📦 Installation via pfSense Package Manager

1. Navigate to: `System > Package Manager > Available Packages`
2. Search for `Suricata` and install
3. Reboot pfSense after installation  
![Suricata Install](./img/install_suricata.png)

---

## ⚙️ Configuration Steps

1. Go to `Services > Suricata`
2. Create a new interface and assign to `WAN`
3. In `Global Settings`, select:
   - Rules: ✅ **Enable ET Open Rules**  
   ![ET Open Rules](./img/ETOpen rules.png)
4. In `Updates`, update your rule set:  
   Click `FORCE` to download the rules  
   ![ET Rule Download](./img/Install_Emerging Threats open rules.png)
5. After downloading, go to your interface settings (`WAN RULES`):
   - ✅ **Enable All Rules**
   - ✅ **Log Alerts to System Logs**

6. Save and apply configuration

---

## 🔍 Gotchas / Issues

- **Rules were downloaded but not active** until manually enabled in the interface settings
- IPS mode is disabled (only IDS active for learning purposes)
