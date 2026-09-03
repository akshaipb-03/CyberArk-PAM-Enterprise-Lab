import csv
import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "accounts.csv"
OUTPUT_FILE = BASE_DIR / "onboarding_results.json"


def validate_account(account):
    required_fields = ["name", "username", "address", "safe", "platform"]

    missing = [
        field for field in required_fields
        if not account.get(field, "").strip()
    ]

    if missing:
        return False, f"Missing fields: {', '.join(missing)}"

    if account["platform"] not in ["Unix", "Windows"]:
        return False, f"Unsupported platform: {account['platform']}"

    return True, "Validation successful"


def onboard_account(account):
    print("\n" + "=" * 50)
    print(f"Processing: {account['name']}")

    valid, message = validate_account(account)

    if not valid:
        print(f"FAILED: {message}")
        return {
            **account,
            "status": "FAILED",
            "message": message
        }

    print("✓ Validating account")
    print(f"✓ Selecting Safe: {account['safe']}")
    print(f"✓ Selecting platform: {account['platform']}")
    print(f"✓ Onboarding username: {account['username']}")
    print(f"✓ Target address: {account['address']}")
    print("✓ Simulating password management assignment")
    print("✓ Simulating session management assignment")

    return {
        **account,
        "status": "SUCCESS",
        "onboarded_at": datetime.now().isoformat(),
        "message": "Account ready for CyberArk onboarding"
    }


def main():
    results = []

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for account in reader:
            results.append(onboard_account(account))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as jsonfile:
        json.dump(results, jsonfile, indent=4)

    successful = sum(
        1 for result in results
        if result["status"] == "SUCCESS"
    )

    print("\n" + "=" * 50)
    print("ONBOARDING SUMMARY")
    print(f"Successful: {successful}/{len(results)}")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
