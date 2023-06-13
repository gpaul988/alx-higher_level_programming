#!/usr/bin/python3
# Graham S. Paul (3-print_reversed_list_integer.py)

"""Pulls all integers of list in reverse order"""

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in my_list[::-1]:
        print("{:d}".format(i))
