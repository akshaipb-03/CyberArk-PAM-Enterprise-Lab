import csv
import json
import socket
import time
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "accounts.local.csv"
REPORT_FILE = BASE_DIR / "pam_precheck_results.json"


PLATFORM_CONFIG = {
    "Unix": {
        "safe": "UNIX-ADMIN-SAFE",
        "port": 22,
        "protocol": "SSH",
    },
    "Windows": {
        "safe": "WIN-ADMIN-SAFE",
        "port": 3389,
        "protocol": "RDP",
    },
}


def check_port(
    host,
    port,
    timeout=5,
    retries=3,
    retry_delay=2,
):
    """
    Check whether a TCP port is reachable.

    Uses multiple attempts to reduce false negatives caused
    by temporary network instability.

    Returns:
        tuple:
            reachable
            connection_error
            attempts_used
    """

    last_error = None

    for attempt in range(1, retries + 1):

        print(f"  Connection attempt {attempt}/{retries}")

        try:
            with socket.create_connection(
                (host, port),
                timeout=timeout,
            ):
                print("  Connection successful")

                return True, None, attempt

        except socket.timeout:
            last_error = "Connection timed out"

        except ConnectionRefusedError:
            last_error = "Connection was refused"

        except OSError as error:
            last_error = f"Network error: {error}"

        print(
            f"  Attempt {attempt} failed: "
            f"{last_error}"
        )

        if attempt < retries:
            print(
                f"  Waiting {retry_delay} seconds "
                "before retry..."
            )

            time.sleep(retry_delay)

    return False, last_error, retries


def validate_account(account):
    """
    Validate required PAM onboarding information.
    """

    errors = []

    required_fields = [
        "name",
        "username",
        "address",
        "safe",
        "platform",
    ]

    for field in required_fields:

        if not account.get(field, "").strip():

            errors.append(
                f"Missing required field: {field}"
            )

    platform = account.get("platform")

    if platform not in PLATFORM_CONFIG:

        errors.append(
            f"Unsupported platform: {platform}"
        )

        return errors

    expected_safe = PLATFORM_CONFIG[platform]["safe"]

    if account.get("safe") != expected_safe:

        errors.append(
            "Safe mapping mismatch. "
            f"Expected: {expected_safe}"
        )

    return errors


def precheck_account(account):
    """
    Perform a complete PAM onboarding pre-check.
    """

    print("\n" + "=" * 60)
    print(
        f"PAM PRE-CHECK: "
        f"{account.get('name', 'UNKNOWN')}"
    )
    print("=" * 60)

    errors = validate_account(account)

    platform = account.get("platform")
    config = PLATFORM_CONFIG.get(platform)

    if not config:

        print("Result: FAILED")

        return {
            **account,
            "status": "FAILED",
            "checked_at": datetime.now().isoformat(),
            "errors": errors,
        }

    host = account.get(
        "address",
        "",
    ).strip()

    port = config["port"]
    protocol = config["protocol"]

    print(
        f"Account: "
        f"{account.get('username')}"
    )

    print(f"Target: {host}")

    print(f"Platform: {platform}")

    print(
        f"Safe: "
        f"{account.get('safe')}"
    )

    print(
        f"Expected Protocol: {protocol}"
    )

    print(
        f"Checking Port: {port}"
    )

    if host:

        (
            reachable,
            connection_error,
            attempts_used,
        ) = check_port(
            host,
            port,
            timeout=5,
            retries=3,
            retry_delay=2,
        )

    else:

        reachable = False

        connection_error = (
            "Target address is missing"
        )

        attempts_used = 0

    if reachable:

        print(
            "Network Status: REACHABLE"
        )

    else:

        print(
            "Network Status: UNREACHABLE"
        )

        errors.append(
            f"Target port {port} "
            f"is unreachable: "
            f"{connection_error}"
        )

    if errors:

        status = "NOT_READY"

        print(
            "\nResult: NOT READY"
        )

        for error in errors:

            print(
                f"  - {error}"
            )

    else:

        status = "READY"

        print(
            "\nResult: READY FOR ONBOARDING"
        )

    return {
        **account,
        "status": status,
        "port": port,
        "protocol": protocol,
        "network_reachable": reachable,
        "connection_attempts": attempts_used,
        "checked_at": datetime.now().isoformat(),
        "errors": errors,
    }


def main():
    """
    Run PAM onboarding pre-checks
    for all accounts.
    """

    results = []

    print("\n" + "=" * 60)
    print(
        "SECURECORP PAM ONBOARDING PRE-CHECK"
    )
    print("=" * 60)

    print(
        "Started: "
        f"{datetime.now().isoformat(timespec='seconds')}"
    )

    try:

        with open(
            CSV_FILE,
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            for account in reader:

                result = precheck_account(
                    account
                )

                results.append(
                    result
                )

    except FileNotFoundError:

        print("\nERROR")

        print(
            "Local inventory not found: "
            f"{CSV_FILE}"
        )

        return

    except Exception as error:

        print(
            f"\nUnexpected error: {error}"
        )

        return

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            results,
            file,
            indent=4,
        )

    ready_count = sum(
        1
        for result in results
        if result["status"] == "READY"
    )

    not_ready_count = sum(
        1
        for result in results
        if result["status"] != "READY"
    )

    print("\n" + "=" * 60)

    print(
        "PAM ONBOARDING PRE-CHECK SUMMARY"
    )

    print("=" * 60)

    print(
        f"Total targets: {len(results)}"
    )

    print(
        f"Ready: {ready_count}"
    )

    print(
        f"Not ready: {not_ready_count}"
    )

    print(
        f"Report: {REPORT_FILE}"
    )

    if results and ready_count == len(results):

        print(
            "\nOVERALL STATUS: "
            "ALL TARGETS READY"
        )

    else:

        print(
            "\nOVERALL STATUS: "
            "ACTION REQUIRED"
        )


if __name__ == "__main__":
    main()
