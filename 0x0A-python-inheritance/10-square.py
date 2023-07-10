#!/usr/bin/python3
# Graham S. Paul (10-square.py)
"""
Holds rear class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Asummed from Rectangle, which assumed from BaseGeometry
    """
    def __init__(self, size):
        """
        Assumes size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
