#!/usr/bin/python3
# Graham S. Paul (5-square.py)
"""Explains class square"""


class Square:
    """Shows a square"""
    def __init__(self, size=0):
        """Boots fresh square"""
        self.size = size

    @property
    def size(self):
        """Acquire contemporary size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Calibrate contemporary size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retrieves contemporary area of square"""
        return self.__size ** 2

    def my_print(self):
        """Pullssquare using #"""
        for i in range(self.size):
            print("#" * self.size)

        if not self.size:
            print()
