#!/usr/bin/python3
# Graham S. Paul (1-write_file.py)
"""
Notes to text file and retrieves num chars written
"""


def write_file(filename="", text=""):
    """Note to text file and retrieves num chars written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
