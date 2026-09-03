import csv
import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

INVENTORY_FILE = BASE_DIR / "accounts.csv"

RESULT_FILES = {
    "onboarding": BASE_DIR / "onboarding_results.json",
    "rotation": BASE_DIR / "final_rotation_results.json",
    "reconciliation": BASE_DIR / "reconciliation_results.json",
    "precheck": BASE_DIR / "pam_precheck_results.json",
}

REPORT_FILE = BASE_DIR / "pam_operations_audit.json"


def load_json_file(file_path):
    """Load a JSON results file safely."""

    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print(f"WARNING: Invalid JSON file: {file_path.name}")
        return []

    except OSError as error:
        print(
            f"WARNING: Could not read "
            f"{file_path.name}: {error}"
        )
        return []


def load_inventory():
    """Load the non-sensitive account inventory."""

    accounts = []

    if not INVENTORY_FILE.exists():
        print(
            f"WARNING: Inventory not found: "
            f"{INVENTORY_FILE.name}"
        )
        return accounts

    with open(
        INVENTORY_FILE,
        newline="",
        encoding="utf-8",
    ) as file:

        reader = csv.DictReader(file)

        for account in reader:
            accounts.append(account)

    return accounts


def get_account_key(account):
    """Create a consistent account identifier."""

    return (
        account.get("name")
        or account.get("account")
        or account.get("username")
        or account.get("user")
        or "UNKNOWN"
    )


def index_results(results):
    """Index result records by account name."""

    indexed = {}

    if not isinstance(results, list):
        return indexed

    for result in results:
        if not isinstance(result, dict):
            continue

        key = get_account_key(result)
        indexed[key] = result

    return indexed


def get_status(result):
    """Return a normalized status."""

    if not result:
        return "NO_DATA"

    return result.get(
        "status",
        result.get("result", "UNKNOWN"),
    )


def get_errors(result):
    """Extract errors from a result record."""

    if not result:
        return []

    errors = result.get("errors", [])

    if isinstance(errors, list):
        return errors

    if errors:
        return [str(errors)]

    error = result.get("error")

    if error:
        return [str(error)]

    return []


def main():

    print("\n" + "=" * 65)
    print("SECURECORP PAM OPERATIONS AUDIT REPORT")
    print("=" * 65)

    inventory = load_inventory()

    result_data = {}

    for name, file_path in RESULT_FILES.items():

        result_data[name] = load_json_file(
            file_path
        )

        print(
            f"Loaded {name}: "
            f"{len(result_data[name])} record(s)"
        )

    indexes = {
        name: index_results(data)
        for name, data in result_data.items()
    }

    accounts = []

    for account in inventory:

        account_key = get_account_key(account)

        onboarding = indexes["onboarding"].get(
            account_key
        )

        rotation = indexes["rotation"].get(
            account_key
        )

        reconciliation = indexes["reconciliation"].get(
            account_key
        )

        precheck = indexes["precheck"].get(
            account_key
        )

        account_audit = {
            "name": account.get("name"),
            "username": account.get("username"),
            "address": account.get("address"),
            "platform": account.get("platform"),
            "safe": account.get("safe"),

            "onboarding_status": get_status(
                onboarding
            ),

            "password_rotation_status": get_status(
                rotation
            ),

            "reconciliation_status": get_status(
                reconciliation
            ),

            "precheck_status": get_status(
                precheck
            ),

            "precheck_network_reachable": (
                precheck.get(
                    "network_reachable",
                    None,
                )
                if precheck
                else None
            ),

            "connection_attempts": (
                precheck.get(
                    "connection_attempts",
                    None,
                )
                if precheck
                else None
            ),

            "issues": (
                get_errors(onboarding)
                + get_errors(rotation)
                + get_errors(reconciliation)
                + get_errors(precheck)
            ),
        }

        accounts.append(account_audit)

    ready_count = sum(
        1
        for account in accounts
        if account["precheck_status"] == "READY"
    )

    total_accounts = len(accounts)

    rotation_issues = sum(
        1
        for account in accounts
        if account[
            "password_rotation_status"
        ]
        not in (
            "SUCCESS",
            "COMPLETED",
            "READY",
            "NO_DATA",
        )
    )

    report = {
        "report_name": "SecureCorp PAM Operations Audit",
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_accounts": total_accounts,
            "targets_ready": ready_count,
            "targets_not_ready": (
                total_accounts - ready_count
            ),
            "rotation_issues": rotation_issues,
        },
        "accounts": accounts,
    }

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
        )

    print("\n" + "=" * 65)
    print("AUDIT SUMMARY")
    print("=" * 65)
    print(
        f"Total Accounts: "
        f"{report['summary']['total_accounts']}"
    )
    print(
        f"Targets Ready: "
        f"{report['summary']['targets_ready']}"
    )
    print(
        f"Targets Not Ready: "
        f"{report['summary']['targets_not_ready']}"
    )
    print(
        f"Rotation Issues: "
        f"{report['summary']['rotation_issues']}"
    )
    print(f"\nReport: {REPORT_FILE}")


if __name__ == "__main__":
    main()
