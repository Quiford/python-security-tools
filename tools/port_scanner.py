#!/usr/bin/env python3
"""
port_scanner.py
A simple TCP port scanner for common services.
Usage: python port_scanner.py
"""

import socket
import sys


# Common ports to scan with their associated services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy",
}


def resolve_target(target: str) -> str:
    """Resolve a hostname or domain to an IP address."""
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"[ERROR] Could not resolve host: {target}")
        sys.exit(1)


def scan_port(ip: str, port: int) -> bool:
    """Attempt a TCP connection to a given IP and port. Return True if open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)  # 1-second timeout to keep scanning fast
    try:
        result = sock.connect_ex((ip, port))
        return result == 0
    except socket.error as e:
        print(f"[ERROR] Socket error on port {port}: {e}")
        return False
    finally:
        sock.close()


def scan_target(target: str) -> None:
    """Scan common ports on the target and display results."""
    ip = resolve_target(target)
    print(f"\n[*] Scanning target: {target} ({ip})")
    print(f"[*] Scanning {len(COMMON_PORTS)} common ports...\n")

    open_count = 0
    print(f"{'PORT':<10}{'STATE':<10}{'SERVICE':<15}")
    print("-" * 35)

    for port, service in sorted(COMMON_PORTS.items()):
        is_open = scan_port(ip, port)
        state = "OPEN" if is_open else "CLOSED"
        if is_open:
            open_count += 1
            print(f"{port:<10}{state:<10}{service:<15}")
        else:
            # Optional: uncomment the next line to show closed ports too
            # print(f"{port:<10}{state:<10}{service:<15}")
            pass

    print("-" * 35)
    print(f"\n[*] Scan complete. {open_count} port(s) open.\n")


def main() -> None:
    """Prompt user for target and run the port scan."""
    print("=" * 40)
    print("     PYTHON PORT SCANNER")
    print("=" * 40)

    target = input("Enter target IP or domain: ").strip()
    if not target:
        print("[ERROR] No target provided. Exiting.")
        sys.exit(1)

    try:
        scan_target(target)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()
