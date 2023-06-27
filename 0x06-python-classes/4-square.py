#!/usr/bin/python3
# Graham S. Paul (4-square.py)
"""Explain class square"""


class Square:
    """Shows a square"""
    def __init__(self, size=0):
        """Boot fresh square"""
        self.size = size

    @property
    def size(self):
        """Acquire current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Calibrate current size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Restores current area of square"""
        return self.__size ** 2
