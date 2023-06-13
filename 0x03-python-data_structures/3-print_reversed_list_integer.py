#!/usr/bin/python3
# Graham S. Paul (3-print_reversed_list_integer.py)

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    for i in my_list[::-1]:
        print("{:d}".format(my_list[i - 1]))
        i -= 1
