#!/usr/bin/python3
# Graham S. Paul (1-element_at.py)

def element_at(my_list, idx):

    """
    Return element from list
    """

    if idx < len(my_list) and idx > -1:
        return my_list[idx]
    return None
