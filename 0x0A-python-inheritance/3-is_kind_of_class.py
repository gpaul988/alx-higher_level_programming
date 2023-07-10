#!/usr/bin/python3
# Graham S. Paul (3-is_kind_of_class.py)
"""
Holds procedure is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Details:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Retrieve:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)
