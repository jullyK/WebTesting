#!/usr/bin/env python

import requests
import re
import urlparse


def extract_links_from(url):
    try:
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)
    except requests.exceptions.ConnectionError:
        pass


def crawl(url):
    href_links = extract_links_from("http://" + url)
    if href_links:
        for link in href_links:
            link = urlparse.urljoin("http://" + url, link)

            if "#" in link:
                link = link.split("#")[0]

            if url in link and link not in target_links:
                target_links.append(link)
                print(link)
                crawl(link)


target_url = "10.0.2.9/mutillidae/"
target_links = []
crawl(target_url)
