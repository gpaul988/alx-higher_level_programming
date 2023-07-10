#!/usr/bin/python3
"""
Holds rear class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Assumes from Rectangle, which was assumed from BaseGeometry
    Procdeure:
        __init__(self, size)
    """
    def __init__(self, size):
        """Boots size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
