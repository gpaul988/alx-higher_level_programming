#!/usr/bin/python3
# Graham S. Paul (7-error_code.py)
"""
Python scriptp that takes in a URL, sends a request to the URL and displays the body of the reponse
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
