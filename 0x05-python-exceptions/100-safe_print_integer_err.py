#!/usr/bin/python3
# Graham S. Paul (100-safe_print_integer_err.py)
from sys import stderr


def safe_print_integer_err(value):
    """Pulls integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)
