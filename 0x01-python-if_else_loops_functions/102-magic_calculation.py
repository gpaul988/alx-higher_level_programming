#!/usr/bin/python3
# Graham S. Paul

def magic_calculation(a, b, c):
    """Tie bytcode given by Holberton School"""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
