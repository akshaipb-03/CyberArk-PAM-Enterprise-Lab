import csv
import socket
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "accounts.local.csv"

PORTS = {
    "Unix": 22,
    "Windows": 3389,
}


def check_port(host, port, timeout=5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main():
    print("=" * 55)
    print("SecureCorp PAM Target Health Check")
    print(f"Time: {datetime.now().isoformat(timespec='seconds')}")
    print("=" * 55)

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for account in reader:
            platform = account["platform"]
            host = account["address"]
            port = PORTS.get(platform)

            print(f"\nTarget: {account['name']}")
            print(f"Host: {host}")
            print(f"Platform: {platform}")
            print(f"Checking TCP port {port}...")

            if check_port(host, port):
                print("Status: HEALTHY")
            else:
                print("Status: UNREACHABLE")


if __name__ == "__main__":
    main()
