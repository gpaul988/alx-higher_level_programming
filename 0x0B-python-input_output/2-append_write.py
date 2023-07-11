#!/usr/bin/python3
# Graham S. Paul (2-append_write.py)
"""
Attach text file and restores num chars included
"""


def append_write(filename="", text=""):
    """Attach text file and restores num chars added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
