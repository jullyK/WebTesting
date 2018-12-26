#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def get_subdomains(target_url):
    results = []
    with open("subdomains.list", "r") as wordlist_file:
        for line in wordlist_file:
            line = line.strip()
            test_url = line + "." + target_url
            result = request(test_url)
            if result:
                print("[+] Discovered subdomain -> " + test_url)
                results.append(test_url)


def get_URL(target_url):
    results = []
    with open("common.txt", "r") as wordlist_file:
        for line in wordlist_file:
            line = line.strip()
            test_url = target_url + "/" + line
            result = request(test_url)
            if result:
                print("[+] Discovered URL -> " + test_url)
                results.append(test_url)


#metasploitable#
url = "10.0.2.9/mutillidae/"

get_subdomains(url)
get_URL(url)
