#!/usr/bin/python3
# Graham S. Paul (101-remove_char_at.py)

def remove_char_at(str, n):
    """Write a mimiced string without nature at location n"""
    i = f"{str[:n]:s}{str[(n + 1):]}" \
        if n >= 0 else str
    return i
