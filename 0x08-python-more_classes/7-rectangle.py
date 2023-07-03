#!/usr/bin/python3
# Graham S. Paul (7-rectangle.py)
"""
Hold rectangle class
"""


class Rectangle():
    """
    Explains rectangle class with a secured attribute width and height
"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Removes rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ removes instance of class """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """ Achiever reverses width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Calibrator Calibrates width if int > 0 """
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

    def area(self):
        """ Reverses width * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Reverses 2*width + 2*height or reverse if width or height is 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Pulls rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ Thread depiction to generate fresh  instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
