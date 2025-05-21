# Subdomain Enumeration Tool

**By Purab Awasthi, Inter ID - ITID0485**

---

## Overview

This Python script identifies active subdomains of a target domain (e.g., youtube.com) by testing a list of potential subdomains. It uses multithreading to perform concurrent HTTP requests, speeding up the enumeration process. The tool is designed as a practical project to understand DNS, HTTP requests, and multithreading concepts in cybersecurity reconnaissance.

---

## Features

- Reads subdomains from a text file (`subdomains.txt`).
- Checks each subdomain by sending HTTP GET requests.
- Utilizes multithreading to speed up the scanning process.
- Handles exceptions gracefully to avoid crashes.
- Saves discovered subdomains to `discovered_subdomains.txt`.

---

## Prerequisites

- Python 3.x installed.
- `requests` library installed (`pip install requests`).

---

## Usage

1. Add the list of potential subdomains to `subdomains.txt` (one subdomain per line).
2. Run the script:

```bash
python subdomain_enum.py
