#!/usr/bin/python3
# Graham S. Paul (6-post_email.py)
"""
Python script that takes in a URL and an email address
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
