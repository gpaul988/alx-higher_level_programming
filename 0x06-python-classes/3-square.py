#!/usr/bin/python3
# Graham S. Paul (3-square.py)
"""Explain a class square"""


class Square:
    """shows a square"""
    def __init__(self, size=0):
        """Boot fresh square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Reverses current square"""
        return self.__size ** 2
