#!/usr/bin/python3
# Graham S. Paul (4-inherits_from.py)
"""
Holds Procedure inherits_from
"""


def inherits_from(obj, a_class):
    """
    Details:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of

    Retrieve:
        True if obj is instance of class that it inherits from or is subcls of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
