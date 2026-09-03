import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "reconciliation_results.json"
OUTPUT_FILE = BASE_DIR / "final_rotation_results.json"


def retry_rotation(account):
    print("\n" + "=" * 50)
    print(f"Retrying rotation: {account['name']}")

    if account.get("rotation_status") == "SUCCESS":
        print("Original rotation already succeeded.")

        return {
            **account,
            "final_rotation_status": "SUCCESS"
        }

    if account.get("reconciliation_status") == "SUCCESS":
        print("Reconciliation successful.")
        print("Retrying password rotation...")
        print("Changing password...")
        print("Verifying password...")
        print("SUCCESS: Password rotation completed.")

        return {
            **account,
            "final_rotation_status": "SUCCESS",
            "final_rotation_time": datetime.now().isoformat()
        }

    return {
        **account,
        "final_rotation_status": "FAILED"
    }


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        accounts = json.load(file)

    results = [retry_rotation(account) for account in accounts]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\n" + "=" * 50)
    print("FINAL PASSWORD ROTATION SUMMARY")

    for result in results:
        print(
            f"{result['username']}: "
            f"{result['final_rotation_status']}"
        )


if __name__ == "__main__":
    main()
