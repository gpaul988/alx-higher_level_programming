#!/usr/bin/python3
# Graham S. Paul (7-update_dictionary.py)
def update_dictionary(a_dictionary, key, value):
    """Change or include key/value pairs in dictionary"""
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    a_dictionary.update({key: value})

    return a_dictionary
