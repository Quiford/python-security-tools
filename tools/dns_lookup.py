#!/usr/bin/env python3
"""
dns_lookup.py
Query DNS records for a target domain.
Usage: python dns_lookup.py
"""

import sys

import dns.resolver
import dns.exception


def query_record(domain: str, record_type: str) -> list:
    """Query a specific DNS record type and return a list of results."""
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return []
    except dns.exception.DNSException as e:
        print(f"[ERROR] DNS query failed for {record_type}: {e}")
        return []


def dns_lookup(domain: str) -> None:
    """Query and display A, MX, NS, and TXT records for a domain."""
    print(f"\n[*] Querying DNS records for: {domain}\n")

    record_types = ["A", "MX", "NS", "TXT"]

    for rtype in record_types:
        results = query_record(domain, rtype)
        print(f"    {rtype} Records:")
        if results:
            for result in results:
                print(f"        {result}")
        else:
            print("        No records found.")
        print()


def main() -> None:
    """Prompt user for domain and run lookup."""
    print("=" * 40)
    print("       DNS LOOKUP TOOL")
    print("=" * 40)

    domain = input("Enter domain (e.g., example.com): ").strip()
    if not domain:
        print("[ERROR] No domain provided. Exiting.")
        sys.exit(1)

    try:
        dns_lookup(domain)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
