#!/usr/bin/python3
# Graham S. Paul (5-hbtn_header.py)
"""
Python script that takes in a URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
