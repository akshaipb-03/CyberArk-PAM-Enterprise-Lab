# SecureCorp Privileged Account Onboarding

## Account 1 — Linux Administrator

### Account Details

| Field | Value |
|---|---|
| Username | pamadmin |
| Address | LINUX-SRV01 Private IP |
| Safe | UNIX-ADMIN-SAFE |
| Platform | Unix |
| Access Method | SSH |
| Privilege | sudo |
| Password Management | CPM |
| Session Management | PSM |

### Onboarding Process

1. Create or select `UNIX-ADMIN-SAFE`.
2. Select the appropriate Unix platform.
3. Add username `pamadmin`.
4. Add the target's private IP address.
5. Store the credential in CyberArk.
6. Configure account verification.
7. Configure password rotation.
8. Enable session management through PSM.
9. Test privileged access.

---

## Account 2 — Windows Administrator

### Account Details

| Field | Value |
|---|---|
| Username | winadmin |
| Address | WIN-SRV01 Private IP |
| Safe | WIN-ADMIN-SAFE |
| Platform | Windows |
| Access Method | RDP |
| Privilege | Local Administrator |
| Password Management | CPM |
| Session Management | PSM |

### Onboarding Process

1. Create or select `WIN-ADMIN-SAFE`.
2. Select the appropriate Windows platform.
3. Add username `winadmin`.
4. Add the target's private IP address.
5. Store the credential in CyberArk.
6. Configure account verification.
7. Configure password rotation.
8. Enable RDP session management through PSM.
9. Test privileged access.

---

# Password Management Lifecycle

Discovery
    ↓
Onboarding
    ↓
Verification
    ↓
Password Change
    ↓
Password Reconciliation
    ↓
Audit
