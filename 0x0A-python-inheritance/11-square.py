#!/usr/bin/python3
"""
Holds rear class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Assumed from Rectangle, which was assumed from BaseGeometry
    Procedure:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """Assumes size
        Args:
            size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Pulls [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
