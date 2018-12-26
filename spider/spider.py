#!/usr/bin/env python

import requests
import re
import urlparse


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


target_url = "10.0.2.9/mutillidae/"
href_links = extract_links_from("http://" + target_url)
for link in href_links:
    link = urlparse.urljoin("http://" + target_url, link)
    if target_url in link:
        print link
