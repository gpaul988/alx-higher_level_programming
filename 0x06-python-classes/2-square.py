#!/usr/bin/python3
# Graham S. Paul (2-square.py)
"""Explain a class Square"""


class Square:
    """Show a square"""
    def __init__(self, size=0):
        """Boot fresh square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
