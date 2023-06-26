#!/usr/bin/python3
# Graham S. Paul (3-safe_print_dvision.py)
def safe_print_division(a, b):
    """Restores Division a by b"""
    quot = None
    try:
        quot = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(quot))
        return quot
