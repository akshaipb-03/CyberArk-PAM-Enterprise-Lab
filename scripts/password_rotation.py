import json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "onboarding_results.json"
OUTPUT_FILE = BASE_DIR / "password_rotation_results.json"


def rotate_password(account):
    print("\n" + "=" * 50)
    print(f"Starting password rotation: {account['name']}")

    # Simulate a failure for the Windows account
    if account["username"] == "winadmin":
        print("Connecting to target...")
        print("Validating privileged account...")
        print("ERROR: Password change failed")
        print("Reason: Target system rejected the password change")

        return {
            **account,
            "rotation_status": "FAILED",
            "error": "Target system rejected the password change",
            "rotation_time": datetime.now().isoformat()
        }

    print("Connecting to target...")
    print("Changing password...")
    print("Verifying password...")
    print("SUCCESS: Password rotation completed")

    return {
        **account,
        "rotation_status": "SUCCESS",
        "rotation_time": datetime.now().isoformat()
    }


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        accounts = json.load(file)

    results = []

    for account in accounts:
        if account["status"] == "SUCCESS":
            results.append(rotate_password(account))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\n" + "=" * 50)
    print("PASSWORD ROTATION SUMMARY")

    for result in results:
        print(
            f"{result['username']}: "
            f"{result['rotation_status']}"
        )

    print(f"\nResults saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
