#!/usr/bin/python3
# Graham S. Paul (101-locked_class.py)
"""
Closed class
"""


class LockedClass:
    """
    Intercepts clients from generating fresh instace
    dynamically
    """

    __slots__ = "first_name"
