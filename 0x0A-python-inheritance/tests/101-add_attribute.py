#!/usr/bin/python3
# Graham S. Paul (101-add_attribute.py)
"""
Holds purpose that includes fresh ascribed if feasible
"""


def add_attribute(obj, attribute, value):
    """
    Includes ascribed to object if feasible
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
