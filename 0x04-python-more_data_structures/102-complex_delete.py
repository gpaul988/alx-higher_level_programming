#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Erase complex keys with specific value in dictionary"""
    keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys.append(i)

    for i in keys:
        a_dictionary.pop(i)

    return a_dictionary
