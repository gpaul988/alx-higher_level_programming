#!/usr/bin/python3
# Graham S. Paul (10-square.py)
"""
Holds rear class BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Constitute a square.
    """

    def __init__(self, size):
        """
        Boots a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Retrieves a string constitution of the Square example.

        Retrieves:
            str: String constitution of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
