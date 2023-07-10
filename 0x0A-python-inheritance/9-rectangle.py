#!/usr/bin/python3
# Graham S. Paul (9-rectangle.py)
"""
Holds rear class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Assumed from BaseGeometry
    Procedures:
        __init__(self, width, height)
        area(self)
        __str__
    """
    def __init__(self, width, height):
        """Logically boots width and height
        Args:
            width (int): private
            height (int): private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Increases rear void procedure and retrieves area"""
        return self.__width * self.__height

    def __str__(self):
        """ Pulls [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
