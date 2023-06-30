#!/usr/bin/python3
# Graham S. Paul (0-add_integer.py)
"""
Holds a technique which reverses an int sum
Allows two values, whether int or float, and assigns them to int before including them
"""


def add_integer(a, b=98):
    """
    Reverses the int addition (a+b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
