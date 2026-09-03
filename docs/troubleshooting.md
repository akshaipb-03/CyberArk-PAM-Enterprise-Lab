# SecureCorp PAM Troubleshooting Runbook

## Incident

Password rotation failed for the Windows privileged account `winadmin`.

## Alert

Password change failed.

## Investigation

1. Confirm the account is active.
2. Confirm the account belongs to the local Administrators group.
3. Confirm the Windows target is reachable.
4. Validate network connectivity.
5. Verify password policy requirements.
6. Check whether the account is locked.
7. Review CPM logs in a real CyberArk environment.
8. Verify the password stored in the Vault.
9. Use a reconciliation account if configured.

## Simulated Root Cause

The target system rejected the password change.

## Remediation

1. Identify the cause of rejection.
2. Correct the account or platform configuration.
3. Synchronize the credential.
4. Re-run password rotation.
5. Verify successful authentication.

## Evidence

- Initial rotation: FAILED
- Investigation completed
- Reconciliation performed
- Rotation retried
- Final status: SUCCESS
