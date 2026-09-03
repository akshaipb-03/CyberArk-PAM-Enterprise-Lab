<div align="center">

# 🛡️ CyberArk PAM Enterprise Lab

### Privileged Access Management • AWS • Python • Linux • Windows

[![CyberArk Concepts](https://img.shields.io/badge/CyberArk-PAM-blue?style=for-the-badge&logo=cyberark&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](#)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#)
[![Windows](https://img.shields.io/badge/Windows-RDP-0078D4?style=for-the-badge&logo=windows&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Project-Complete-success?style=for-the-badge)](#)

<br>

> **A hands-on Privileged Access Management lab demonstrating privileged account onboarding, password lifecycle operations, reconciliation, connectivity validation, and centralized PAM audit reporting.**

</div>

---

# 📌 Project Overview

This project is a **CyberArk-inspired Privileged Access Management (PAM) enterprise lab** built to understand how privileged accounts are managed throughout their operational lifecycle.

The lab combines **real AWS infrastructure** with **Python automation** and PAM concepts including:

🔐 Safe design  
👤 Privileged account onboarding  
🔄 Password rotation  
🚨 Rotation failure handling  
🛠️ Account reconciliation  
🔁 Retry workflows  
❤️ Target health checking  
📡 SSH and RDP connectivity validation  
📊 Centralized PAM operations reporting  

---

# 🎯 Project Objective

The goal of this project is to simulate the operational workflow of a PAM engineer managing privileged accounts.

```text
        ┌───────────────────────┐
        │   ACCOUNT INVENTORY   │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   PAM SAFE DESIGN     │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ ACCOUNT ONBOARDING    │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ PASSWORD ROTATION     │
        └───────────┬───────────┘
                    │
             ┌──────┴──────┐
             │             │
             ▼             ▼
         SUCCESS        FAILURE
             │             │
             │             ▼
             │      RECONCILIATION
             │             │
             │             ▼
             │       RETRY ROTATION
             │             │
             └──────┬──────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ HEALTH + PRE-CHECK    │
        └───────────┬───────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │ PAM OPERATIONS AUDIT  │
        └───────────────────────┘
```

---

# 🏗️ Architecture

```text
                              👨‍💻
                        PAM OPERATOR
                           macOS
                              │
                              ▼
                   ┌────────────────────┐
                   │  PYTHON AUTOMATION │
                   └─────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
    ┌───────────┐      ┌───────────┐      ┌─────────────┐
    │ ONBOARDING│      │ PRE-CHECK │      │ AUDIT REPORT│
    │ AUTOMATION│      │ & HEALTH  │      │ AGGREGATION │
    └─────┬─────┘      └─────┬─────┘      └─────────────┘
          │                  │
          └──────────┬───────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐
 │ 🐧 LINUX EC2    │       │ 🪟 WINDOWS EC2  │
 │                 │       │                 │
 │ User: pamadmin  │       │ User: winadmin  │
 │ Protocol: SSH   │       │ Protocol: RDP   │
 │ Port: 22        │       │ Port: 3389      │
 └─────────────────┘       └─────────────────┘
        │                         │
        ▼                         ▼
 UNIX-ADMIN-SAFE          WIN-ADMIN-SAFE
```

---

# 🧰 Technology Stack

| Category | Technologies |
|---|---|
| ☁️ Cloud | AWS EC2 |
| 🐧 Linux | Ubuntu |
| 🪟 Windows | Windows Server |
| 🔐 PAM Concepts | CyberArk Safes, Platforms, Rotation, Reconciliation |
| 🐍 Automation | Python |
| 📡 Linux Access | SSH / TCP 22 |
| 🖥️ Windows Access | RDP / TCP 3389 |
| 📄 Data | CSV + JSON |
| 🔀 Version Control | Git + GitHub |
| 🌐 Networking | TCP Socket Validation |

---

# 🔐 PAM Safe Design

Privileged accounts are separated based on operating system and administrative function.

| Safe | Platform | Account Type | Protocol |
|---|---|---|---|
| 🟦 `UNIX-ADMIN-SAFE` | Unix | Linux Administrator | SSH / 22 |
| 🟨 `WIN-ADMIN-SAFE` | Windows | Windows Administrator | RDP / 3389 |

### Design Principles

- 🔒 Separation of privileged accounts
- 🎯 Platform-specific management
- 🔄 Independent password lifecycle workflows
- 🛡️ Least privilege concepts
- 📊 Clear audit boundaries

---

# 🔄 PAM Operational Lifecycle

## 1️⃣ Account Onboarding

The onboarding workflow validates and assigns:

```text
Account
   │
   ├──► Safe
   │
   ├──► Platform
   │
   └──► Password Management Workflow
```

Run:

```bash
python3 scripts/onboard_accounts.py
```

---

## 2️⃣ Password Rotation

The password lifecycle simulates:

```text
START
  │
  ▼
PASSWORD CHANGE
  │
  ▼
PASSWORD VERIFICATION
  │
  ├──── SUCCESS ────► COMPLETED
  │
  └──── FAILURE ────► RECONCILIATION
```

Run:

```bash
python3 scripts/password_rotation.py
```

---

## 3️⃣ Rotation Failure & Reconciliation

A password rotation failure is intentionally reproduced to demonstrate troubleshooting.

```text
🚨 Rotation Failure
        │
        ▼
🔍 Investigate
        │
        ▼
🔐 Validate Password Policy
        │
        ▼
🛠️ Reconcile Account
        │
        ▼
🔁 Retry Rotation
        │
        ▼
✅ Verify Result
```

Run:

```bash
python3 scripts/reconcile_account.py
```

Then:

```bash
python3 scripts/retry_rotation.py
```

---

# ❤️ Target Health Check

The project validates connectivity to real AWS targets.

| Target | Protocol | Port |
|---|---|---:|
| 🐧 Linux EC2 | SSH | 22 |
| 🪟 Windows EC2 | RDP | 3389 |

Run:

```bash
python3 scripts/health_check.py
```

Example:

```text
LINUX TARGET: ONLINE
WINDOWS TARGET: ONLINE

HEALTH CHECK COMPLETE
```

---

# 🧪 PAM Onboarding Pre-Check

Before onboarding, the automation validates:

- ✅ Required account information
- ✅ Platform mapping
- ✅ Safe assignment
- ✅ Target connectivity
- ✅ SSH availability
- ✅ RDP availability

Run:

```bash
python3 scripts/pam_precheck.py
```

Example successful output:

```text
============================================================

SECURECORP PAM ONBOARDING PRE-CHECK

============================================================

PAM PRE-CHECK: Linux Administrator

Network Status: REACHABLE
Result: READY FOR ONBOARDING

PAM PRE-CHECK: Windows Administrator

Network Status: REACHABLE
Result: READY FOR ONBOARDING

============================================================

Total targets: 2
Ready: 2
Not ready: 0

OVERALL STATUS: ALL TARGETS READY
```

---

# 🔁 Resilient Connectivity Validation

During testing, the Linux SSH target demonstrated intermittent connectivity.

A 10-attempt test produced both:

🟢 Successful connections  
🔴 Connection timeouts  

### Initial Design

```text
1 Connection Attempt
        │
        ├── SUCCESS → READY
        │
        └── FAILURE → NOT READY
```

### Improved Design

```text
Connection Attempt 1
        │
        ▼
   SUCCESS? ─── YES ───► READY
        │
       NO
        │
        ▼
Connection Attempt 2
        │
       ...
        │
        ▼
Connection Attempt 3
        │
        ▼
FINAL STATUS
```

The improved pre-check includes:

- 🔁 Multiple retries
- ⏱️ Configurable timeout
- 💤 Retry delay
- 📝 Connection attempt tracking
- 🚨 Detailed error reporting

> **Engineering lesson:** Retry logic reduces false negatives from temporary network instability, but persistent connectivity problems still require investigation.

---

# 📊 PAM Operations Audit Report

The centralized audit automation aggregates multiple PAM workflows.

```text
ACCOUNT INVENTORY
       │
       ├──────────────┐
       ▼              ▼
ONBOARDING      PASSWORD ROTATION
       │              │
       ▼              ▼
PRE-CHECK       RECONCILIATION
       │              │
       └───────┬──────┘
               ▼
     PAM OPERATIONS AUDIT
               │
               ▼
         JSON REPORT
```

Run:

```bash
python3 scripts/pam_audit_report.py
```

Example:

```text
Total Accounts: 2
Targets Ready: 2
Targets Not Ready: 0
Rotation Issues: 0
```

---

# 📁 Project Structure

```text
CyberArk-PAM-Enterprise-Lab/
│
├── 📄 README.md
├── 🔒 .gitignore
│
├── 📂 docs/
│   ├── 📘 account-inventory.md
│   ├── 📘 account-onboarding.md
│   ├── 🏗️ architecture.md
│   ├── 🔐 safe-design.md
│   └── 🛠️ troubleshooting.md
│
└── 📂 scripts/
    ├── 📋 accounts.csv
    ├── 🐍 onboard_accounts.py
    ├── 🔄 password_rotation.py
    ├── 🛠️ reconcile_account.py
    ├── 🔁 retry_rotation.py
    ├── ❤️ health_check.py
    ├── 🧪 pam_precheck.py
    └── 📊 pam_audit_report.py
```

---

# 🔒 Security Controls

The repository is designed to avoid committing sensitive information.

### ❌ Not committed to GitHub

- Private keys
- `.pem` files
- Passwords
- Secrets
- Real target inventory
- Generated operational reports containing target information

Example local file:

```text
scripts/accounts.local.csv
```

is excluded using:

```text
.gitignore
```

Secret scanning can be performed with:

```bash
grep -RniE "AKIA|SECRET_ACCESS_KEY|PRIVATE KEY|BEGIN RSA|password[[:space:]]*=[[:space:]]*['\"]" . \
--exclude-dir=.git \
--exclude-dir=__pycache__
```

---

# 🧠 Skills Demonstrated

<div align="center">

| 🔐 PAM | ☁️ Cloud | 🐍 Automation | 🛠️ Operations |
|---|---|---|---|
| Safe Design | AWS EC2 | Python | Troubleshooting |
| Platform Mapping | Security Groups | CSV | Retry Logic |
| Account Onboarding | SSH | JSON | Error Handling |
| Password Rotation | RDP | Socket Programming | Health Checks |
| Reconciliation | Networking | Audit Reporting | Git/GitHub |

</div>

---

# 💡 Key Learning Outcomes

Through this project, I gained practical experience with:

- Designing a PAM workflow
- Separating privileged accounts into Safes
- Mapping accounts to appropriate platforms
- Understanding the password rotation lifecycle
- Investigating password rotation failures
- Performing account reconciliation
- Managing Linux and Windows targets
- Troubleshooting AWS network connectivity
- Building resilient Python automation
- Creating centralized operational reporting
- Protecting sensitive information in Git repositories

---

# ⚠️ Disclaimer

> This is an educational **CyberArk-inspired PAM lab**.

This project **does not claim to deploy a production CyberArk environment**.

It does not include:

- CyberArk Digital Vault
- CPM
- PVWA
- PSM
- Licensed CyberArk components

The project uses real AWS Linux and Windows targets, while privileged account lifecycle workflows are simulated through custom Python automation.

---

# 🎤 Interview Summary

> **“I built a hands-on CyberArk-inspired PAM lab using real AWS Linux and Windows targets. I designed Safe and platform mappings, automated privileged account onboarding, simulated password rotation and reconciliation workflows, added SSH and RDP connectivity validation, and built centralized PAM audit reporting. During testing, I discovered intermittent SSH connectivity, collected evidence through repeated network tests, and improved the onboarding pre-check using retry-based validation.”**

---

# 🚀 Future Improvements

- [ ] Integrate CyberArk APIs
- [ ] Add real CyberArk PAM components
- [ ] Add Entra ID / Active Directory integration
- [ ] Build an HTML or web-based dashboard
- [ ] Add GitHub Actions security scanning
- [ ] Add structured logging
- [ ] Add automated unit tests
- [ ] Expand to more PAM target platforms

---

<div align="center">

## 🛡️ Built for Learning Privileged Access Management

### CyberArk Concepts • Cloud • Identity • Automation

⭐ **If you found this project interesting, feel free to star the repository!**

</div>
