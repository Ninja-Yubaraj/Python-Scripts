#!/usr/bin/env python3
#
# Script name: whois.py
# Version: 1.0.0
# Description: A Python script to fetch complete WHOIS details for any domain.
# Dependencies: python-whois
# Github: https://github.com/Ninja-Yubaraj/Python-Scripts
# Gitlab: https://gitlab.com/Ninja-Yubaraj/Python-Scripts
# License: https://gitlab.com/Ninja-Yubaraj/Python-Scripts/LICENSE
# Contributors: Yubaraj Sarkar
import whois
import sys

def get_domain_info(domain_name):
    try:
        w = whois.whois(domain_name)

        print("\n--- WHOIS Lookup Result ---")
        for key in w.keys():
            value = w[key]
            if isinstance(value, list):
                value = ', '.join([str(v) for v in value])
            print(f"{key}: {value}")
        print("\n--- End of Report ---\n")

    except Exception as e:
        print(f"Error retrieving WHOIS info: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        domain = input("Enter a domain name (e.g., google.com): ").strip()
    else:
        domain = sys.argv[1]

    get_domain_info(domain)
