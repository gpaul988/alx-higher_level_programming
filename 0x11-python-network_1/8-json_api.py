#!/usr/bin/python3
# Graham S. Paul (8-json_api.py)
"""
Python script that takes in a letter and sends a post request
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}
    r = requests.post(url, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
