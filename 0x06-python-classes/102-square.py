#!/usr/bin/python3
# Graham S. Paul (102-square.py)
"""Explains class square"""


class Square:
    """Shows Square"""
    def __init__(self, size=0):
        """Boots fresh square"""
        self.size = size

    @property
    def size(self):
        """Acquires contemporary size of square"""
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
        """Restore contemporary area of square"""
        return self.__size ** 2

    def __lt__(self, other):
        """Explain < collation to square"""
        return self.size < other.size

    def __gt__(self, other):
        """Explain > collation to square"""
        return self.size > other.size

    def __ge__(self, other):
        """Explains >= collation to square"""
        return self.size >= other.size

    def __le__(self, other):
        """Explain <= collation to square"""
        return self.size <= other.size

    def __ne__(self, other):
        """Explains != collation to square"""
        return self.size != other.size

    def __eq__(self, other):
        """Explain ++ collation to square"""
        return self.size == other.size
