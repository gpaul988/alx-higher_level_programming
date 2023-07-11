#!/usr/bin/python3
"""
Holds class Student
"""


class Student():
    """
    General Feature:
        first_name
        last_name
        age

    General procedure:
        to_json: redeems its dictionary constitution
    """
    def __init__(self, first_name, last_name, age):
        """
        Boots student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Restores:
            Move all features of json to self
        """
        for k, v in json.items():
            setattr(self, k, v)
