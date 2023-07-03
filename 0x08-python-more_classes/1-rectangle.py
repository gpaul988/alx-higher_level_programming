#!/usr/bin/python3
# Graham S. Paul (1-rectangle.py)
"""
Holds class Rectangle
"""


class Rectangle:
    """
    Explains rectangle class with a secured attribute width and height
    """
    def __init__(self, width=0, height=0):
        """ Boots rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Achiever reverses width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Calibrator calibrates width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Achiever reverses height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Calibrator calibrates height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
