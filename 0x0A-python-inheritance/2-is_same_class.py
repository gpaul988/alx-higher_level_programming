#!/usr/bin/python3
"""
Holds procedure is_same_class
"""


def is_same_class(obj, a_class):
    """
    Detailss:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Retrieves:
        True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class
