#!/usr/bin/python3
# Graham S. Paul (8-rectangle.py)
"""
Holds rear class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Assumed from BaseGeometry
    Procudures:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """Logically boots width and height
        Args:
            width (int): private
            height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
