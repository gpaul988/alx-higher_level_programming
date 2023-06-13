#!/usr/bin/python3
# Graham S. Paul (10-divisible_by_2.py)

def divisible_by_2(my_list=[]):
    """
    Search all Multiples of 2 in list
    """
    new = []
    for i in my_list:
        if i % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
