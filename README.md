# Python Security Tools

A collection of beginner-friendly, professional Python-based cybersecurity and networking utilities focused on automation, reconnaissance, and security analysis.

## Features

- Python
- Networking
- APIs 
- Socket Programming


## Tools Included

| Tool | Description |
|------|-------------|
| `port_scanner.py` | Scan IP addresses or domains for open common ports using raw sockets. |
| `ip_lookup.py` | Retrieve geolocation and network information for an IP address. |
| `whois_lookup.py` | Perform WHOIS lookups on domains. |
| `dns_lookup.py` | Query DNS records (A, MX, NS, TXT) for a domain. |
| `hash_checker.py` | Generate and verify file hashes (MD5, SHA-256). |

## Project Structure

```
python-security-tools/
├── tools/
│   ├── port_scanner.py
│   ├── ip_lookup.py
│   ├── whois_lookup.py
│   ├── dns_lookup.py
│   └── hash_checker.py
├── screenshots/
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Quiford/python-security-tools.git
   cd python-security-tools
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or, if 'pip' is not in PATH:
   py -m pip install -r requirements.txt
   ```

## Usage

All tools are CLI-based and can be run directly:

```bash
# Port Scanner
python tools/port_scanner.py
# or: py tools/port_scanner.py

# IP Lookup
python tools/ip_lookup.py
# or: py tools/ip_lookup.py

# WHOIS Lookup
python tools/whois_lookup.py
# or: py tools/whois_lookup.py

# DNS Lookup
python tools/dns_lookup.py
# or: py tools/dns_lookup.py

# Hash Checker
python tools/hash_checker.py
# or: py tools/hash_checker.py
```

## Requirements

- Python 3.8+
- See `requirements.txt` for package dependencies.

## Disclaimer

These tools are intended for educational purposes and authorized security testing only. Always obtain proper permission before scanning or analyzing networks and systems you do not own.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


## Roadmap

Planned additions:
- Multi-threaded port scanning
- Subdomain enumeration
- URL reputation checker
- Packet analysis utilities
- API integrations
- Improved CLI argument handling

## Author

Afolabi Yusuf Oladipupo.