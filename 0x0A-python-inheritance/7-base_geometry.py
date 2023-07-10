#!/usr/bin/python3
# Graham S. Paul (7-base_geometry.py)
"""
Holds BaseGeometry
"""


class BaseGeometry:
    """
    Procedures:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """Void"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Logical code
        Args:
            name (str): assumed always a string
            value (int): greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
