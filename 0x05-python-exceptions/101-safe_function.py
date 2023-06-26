#!/usr/bin/python3
# Graham S. Paul (101-safe_function.py)
from sys import stderr


def safe_function(fct, *args):
    """Enact a function safely"""
    try:
        return fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return None
