#!/usr/bin/python3
# Graham S. Paul (8-simple_delete.py)
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        a_dictionary.pop(key)

    return a_dictionary
