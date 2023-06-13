#!/usr/bin/python3
#Graham S. Paul (3-print_reversed_list_integer.py)

def print_reversed_list_integer(my_list=[]):
    """pull integers of  list in return order"""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
