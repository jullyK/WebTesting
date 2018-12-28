#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup
import urlparse

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://10.0.2.9/mutillidae/index.php?page=dns-lookup.php"

response = request(target_url)
parsed_html = BeautifulSoup(response.content)

forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    method = form.get("method")
    post_url = urlparse.urljoin(target_url, action)

    print("[+] Form found : " + method + " / " + action)
    post_data = {}
    for html_input in form.findAll("input"):
        input_name = html_input.get("name")
        input_type = html_input.get("type")
        input_value = html_input.get("value")
        print("\t[+] Input Type/Name: " + input_type + " / " + input_name)
        if input_type == "text":
            input_value = "test"
        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
    print(result.content)
