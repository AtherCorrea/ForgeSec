# 🧪 ForgeSec – Validation Cases (Cyber Core)

This folder contains the **Validation Cases** for the Cyber Core module.

Each directory represents a real, self-contained validation unit created to test, observe, and document a specific defensive mechanism in modern cybersecurity systems.

These are not educational labs. They are **authored engineering experiments**, executed with real tools (Suricata, tcpreplay, Scapy), controlled traffic, and structured documentation.

---

## 📂 Structure of a Validation Case

(```text)
<DOMAIN>_<NN>__<descriptor>/
├── <same_name>.md      # Main test case documentation  
├── input.pcap          # (Optional) simulated traffic  
├── eve.json            # Output log (Suricata, Zeek, etc.)  
└── img/                # Screenshots and evidence from the run
(```)

**Example:**

(```text)
IDS_00__tcp-stream-reassembly/
├── IDS_00__tcp-stream-reassembly.md
├── input.pcap
├── eve.json
└── img/
    └── alert-detected.png
(```)

---

## 🧠 Naming Convention

(```text)
<DOMAIN>_<NN>__<short-descriptor>/
(```)

- `DOMAIN`: Technology or subsystem (e.g., IDS, FLOW, TLS, HTTP, SIEM)
- `NN`: Two-digit sequence number based on learning progression
- `short-descriptor`: Clear and technical summary of the test focus

**Examples:**

- `IDS_00__tcp-stream-reassembly`
- `FLOW_01__tracking-timeout-window`
- `SIEM_03__sysmon-dns-correlation`

This structure allows for long-term scalability, easy indexing, and clarity.

---

## 📘 How to Use

- Each directory can be opened, executed, and reviewed independently
- All validations are based on **real execution**, not simulated theory
- Markdown files follow a standardized reasoning structure
- Screenshots, logs, and config snippets reflect real engine behavior

---

## 🔗 Link to Documentation

Each Validation Case is linked to the technical documents that motivated its creation, located at:

(```text)
cyber_core/docs/Learning/<topic>.md
(```)

And each `.md` theory file also links back to its related test cases.

---

## ⚠️ Nothing enters this directory without being executed and truly understood

ForgeSec does not simulate.  
ForgeSec **experiments, observes, documents — and evolves.**
