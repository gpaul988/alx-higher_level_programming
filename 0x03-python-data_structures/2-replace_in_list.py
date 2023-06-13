#!/usr/bin/python3
# Graham s. Paul (2-replapce_in_list.py)

def replace_in_list(my_list, idx, element):
    """change an element of a list at a specific location"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
