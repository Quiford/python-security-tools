#!/usr/bin/env python3
"""
ip_lookup.py
Retrieve geolocation and network data for an IP address.
Usage: python ip_lookup.py
"""

import socket
import sys

import requests


def lookup_ip(ip: str) -> None:
    """Display geolocation and network info for an IP via ip-api.com."""
    print(f"\n[*] Looking up IP: {ip}")

    # Resolve hostname via socket
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        hostname = "Unknown"

    print(f"    Hostname: {hostname}")

    # Fetch geolocation data
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as,query"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return

    if data.get("status") != "success":
        print(f"[ERROR] API error: {data.get('message', 'Unknown error')}")
        return

    print(f"    Query:    {data.get('query', ip)}")
    print(f"    Country:  {data.get('country', 'N/A')}")
    print(f"    Region:   {data.get('regionName', 'N/A')}")
    print(f"    City:     {data.get('city', 'N/A')}")
    print(f"    ZIP:      {data.get('zip', 'N/A')}")
    print(f"    Lat/Lon:  {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
    print(f"    ISP:      {data.get('isp', 'N/A')}")
    print(f"    Org:      {data.get('org', 'N/A')}")
    print(f"    AS:       {data.get('as', 'N/A')}")


def main() -> None:
    """Prompt user for IP and run lookup."""
    print("=" * 40)
    print("       IP LOOKUP TOOL")
    print("=" * 40)

    target = input("Enter IP address: ").strip()
    if not target:
        print("[ERROR] No IP provided. Exiting.")
        sys.exit(1)

    try:
        lookup_ip(target)
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
