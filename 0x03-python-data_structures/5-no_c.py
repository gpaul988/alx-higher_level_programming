#!/usr/bin/python3
# Graham S. Paul (5-no_c.py)

"""Erase all Characters 'c' and 'C' from string"""

def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c.lower() != "c":
            new_string += c
    return new_string
