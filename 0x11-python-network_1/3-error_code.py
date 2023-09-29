#!/usr/bin/python3
# Graham S. Paul (3-error_code.py)
"""
Python script that takes in a URL sends a request to the URL and displays the body
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
