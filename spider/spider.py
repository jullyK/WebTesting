#!/usr/bin/env python

import requests
import re
import urlparse


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


target_url = "10.0.2.9/mutillidae/"
target_links = []

href_links = extract_links_from("http://" + target_url)
for link in href_links:
    link = urlparse.urljoin("http://" + target_url, link)
    if "#" in link:
        link = link.split("#")[0]
    if target_url in link and link not in target_links:
        target_links.append(link)
        print(link)
