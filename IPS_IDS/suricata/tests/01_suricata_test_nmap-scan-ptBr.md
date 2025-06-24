# 🧪 Teste 01 – Nmap Scan contra Windows Server

**Data:** 2025-06-18\
**Responsável:** Ather Correa\
**Ferramenta monitorada:** Suricata IDS\
**Objetivo:** Validar detecção de varredura de portas e fingerprinting usando Nmap

---

## 🌟 Cenário do Teste

| Item                 | Detalhes                      |
| -------------------- | ----------------------------- |
| Atacante             | Kali Linux                    |
| Alvo                 | Windows Server 2022           |
| IDS/Firewall         | pfSense + Suricata (modo IDS) |
| Interface monitorada | LAN (192.168.100.0/24)        |
| IP Atacante          | 192.168.100.100               |
| IP Alvo              | 192.168.100.10                |

---

## 🛠️ Comando Executado

```bash
nmap -A -T4 -sV -O --script vuln 192.168.100.10
```

**Descrição do comando:**

- `-A` = ativa detecção avançada (OS, serviços, scripts NSE)
- `-T4` = velocidade agressiva
- `-sV` = detecção de versão
- `-O` = detecção de sistema operacional
- `--script vuln` = roda scripts NSE de vulnerabilidades conhecidas

---

## 🚨 Alertas Gerados (Suricata)

| Categoria | SID     | Descrição do Alerta                         |
| --------- | ------- | ------------------------------------------- |
| ET SCAN   | 2010937 | Nmap Scripting Engine User-Agent Detected   |



> 🔍 **Nota:** Para esses alertas aparecerem, foi necessário ativar as regras manualmente na aba `WAN` do Suricata.

---

## 📄 Arquivos gerados

| Nome do Arquivo       | Descrição                                |
| --------------------- | ---------------------------------------- |
| `eve.json`            | Log bruto gerado pelo Suricata           |
| `screenshot.png`      | Print do alerta no Suricata (opcional)   |

---

## 📌 Observações

- Suricata estava configurado apenas com as regras baixadas, mas **não ativas**
- Após ativação da categoria `ET Open Scan`, os alertas passaram a aparecer corretamente
- Kali estava na WAN, então o tráfego foi detectado pela interface monitorada

---

## ✅ Conclusão

Teste validou que:

- Suricata está **capturando tráfego da WAN corretamente**
- Regras precisam ser ativas na interface para funcionarem
- O comando Nmap `-A` gera alertas suficientes para simular atividades maliciosas

---