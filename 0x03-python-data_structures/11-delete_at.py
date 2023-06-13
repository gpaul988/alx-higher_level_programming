#!/usr/bin/python3
# Graham S. Paul (11-delete_at.py)

def delete_at(my_list=[], idx=0):
    """
    Eliminate an item at a particular point in list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    del my_list[idx]
    return my_list
