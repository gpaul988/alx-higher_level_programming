#!/usr/bin/python3
# Graham S. Paul (9-print_last_digit.py)

def print_last_digit(number):
    """Pull last digit of number and reinstate it"""
    print(f'{(abs(number) % 10):d}', end='')
    return abs(number) % 10
