#!/usr/bin/python3
# Graham S. Paul (0-read_file.py)
"""
Peruse and pulls contents from file
"""


def read_file(filename=""):
    """peruse and pull  text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
