#!/usr/bin/python3
# Graham S. Paul (2-rectangle.py)
"""
Holds a rectangle class with a secured attribute width and height
"""


class Rectangle:
    """
    Explainis rectangle class with a secured attribute width and height
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
        """ Calibrator Claibrates width if int > 0 """
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
        """ Calibrator claibrates height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Reverses width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Reverses 2*width + 2*height or reverss if width or height is 0 """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)
