#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = ".google.com"
with open("subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        line = line.strip()
        test_url = line + target_url
        result = request(test_url)
        if result:
            print("[+] Discovered subdomain -> " + test_url)
