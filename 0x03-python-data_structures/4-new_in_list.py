#!/usr/bin/python3
# Graham S. Paul (4-new_in_list.py)

"""Change element in a mimiced list at specific location"""

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = []
        for i in my_list:
                new_list.append(i)
        new_list[idx] = element
        return new_list
