# SecureCorp CyberArk Safe Design

## Project
Enterprise Privileged Access Management (PAM) Lab

## Objective
Protect privileged accounts using a least-privilege access model.

---

# Safe 1: UNIX-ADMIN-SAFE

## Purpose
Stores privileged credentials used for Linux administration.

## Accounts

| Account | Target | Access |
|---|---|---|
| pamadmin | LINUX-SRV01 | SSH / sudo |

## Access Permissions

| User / Group | Permission |
|---|---|
| PAM-Admins | Manage Safe |
| Linux-Operations | Retrieve/use accounts |
| Auditors | View/audit only |

---

# Safe 2: WIN-ADMIN-SAFE

## Purpose
Stores privileged credentials used for Windows administration.

## Accounts

| Account | Target | Access |
|---|---|---|
| winadmin | WIN-SRV01 | RDP / local admin |

## Access Permissions

| User / Group | Permission |
|---|---|
| PAM-Admins | Manage Safe |
| Windows-Operations | Retrieve/use accounts |
| Auditors | View/audit only |

---

# Access Model

PAM-Admins
├── UNIX-ADMIN-SAFE
└── WIN-ADMIN-SAFE

Linux-Operations
└── Access to UNIX-ADMIN-SAFE only

Windows-Operations
└── Access to WIN-ADMIN-SAFE only

Auditors
├── Audit access
└── No administrative access

---

# Security Principles

- Least privilege
- Separation of duties
- No shared passwords
- Privileged credentials stored in CyberArk
- Password rotation
- Session monitoring
- Auditable access
