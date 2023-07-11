#!/usr/bin/python3
# Graham S. Paul (9-student.py)
"""
Holds class student
"""


class Student():
    """
    General features:
        first_name
        last_name
        age

    General procedure:
        to_json: redeems its dictionary constitutiion
    """
    def __init__(self, first_name, last_name, age):
        """
        Boots student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Restores dictionary explanation with easy data shape
        """
        return self.__dict__
