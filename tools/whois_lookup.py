#!/usr/bin/env python3
"""
whois_lookup.py
Perform a WHOIS lookup on a domain.
Usage: python whois_lookup.py
"""

import sys

import whois


def whois_lookup(domain: str) -> None:
    """Fetch and display WHOIS information for a domain."""
    print(f"\n[*] Performing WHOIS lookup for: {domain}")

    try:
        w = whois.whois(domain)
    except whois.parser.PywhoisError as e:
        print(f"[ERROR] WHOIS lookup failed: {e}")
        return

    def print_field(label: str, value) -> None:
        """Helper to print a WHOIS field cleanly."""
        if value is None:
            value = "N/A"
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        print(f"    {label:<20}{value}")

    print_field("Registrar:", w.registrar)
    print_field("Creation Date:", w.creation_date)
    print_field("Expiration Date:", w.expiration_date)
    print_field("Updated Date:", w.updated_date)
    print_field("Name Servers:", w.name_servers)
    print_field("Status:", w.status)
    print_field("Organization:", w.org)
    print_field("Country:", w.country)


def main() -> None:
    """Prompt user for domain and run lookup."""
    print("=" * 40)
    print("      WHOIS LOOKUP TOOL")
    print("=" * 40)

    domain = input("Enter domain (e.g., example.com): ").strip()
    if not domain:
        print("[ERROR] No domain provided. Exiting.")
        sys.exit(1)

    try:
        whois_lookup(domain)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
