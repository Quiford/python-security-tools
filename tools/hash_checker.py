#!/usr/bin/env python3
"""
hash_checker.py
Generate and verify file hashes (MD5, SHA-256).
Usage: python hash_checker.py
"""

import hashlib
import sys


def hash_file(filepath: str) -> dict:
    """Generate MD5 and SHA-256 hashes for a file."""
    hashes = {"md5": hashlib.md5(), "sha256": hashlib.sha256()}
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                for h in hashes.values():
                    h.update(chunk)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
        sys.exit(1)
    except PermissionError:
        print(f"[ERROR] Permission denied: {filepath}")
        sys.exit(1)

    return {name: h.hexdigest() for name, h in hashes.items()}


def verify_hash(filepath: str, expected: str, algorithm: str = "sha256") -> None:
    """Verify a file against an expected hash."""
    if algorithm.lower() not in ("md5", "sha256"):
        print("[ERROR] Supported algorithms: md5, sha256")
        sys.exit(1)

    generated = hash_file(filepath)[algorithm.lower()]
    match = generated.lower() == expected.lower()
    status = "MATCH" if match else "MISMATCH"
    print(f"\n    Expected: {expected}")
    print(f"    Computed: {generated}")
    print(f"    Result:   {status}")


def main() -> None:
    """Prompt user and run hash operations."""
    print("=" * 40)
    print("      HASH CHECKER TOOL")
    print("=" * 40)

    print("\n1. Generate hashes")
    print("2. Verify hash")
    choice = input("\nSelect option (1/2): ").strip()

    if choice == "1":
        filepath = input("Enter file path: ").strip()
        result = hash_file(filepath)
        print(f"\n    MD5:    {result['md5']}")
        print(f"    SHA256: {result['sha256']}")
    elif choice == "2":
        filepath = input("Enter file path: ").strip()
        algorithm = input("Enter algorithm (md5/sha256) [default: sha256]: ").strip() or "sha256"
        expected = input("Enter expected hash: ").strip()
        verify_hash(filepath, expected, algorithm)
    else:
        print("[ERROR] Invalid choice. Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
