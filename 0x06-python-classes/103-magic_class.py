#!/usr/bin/python3
# Graham S. Paul (103-magic_class.py)
"""Explain magic class preciselyparallel to bytecode given by Holberton"""
import math


class MagicClass:
    """Boot and explain technique area and cirecumference"""
    def __init__(self, radius=0):
        """Boot Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Restores area of magic class"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Restores circumference of magic class"""
        return 2 * math.pi * self.__radius
