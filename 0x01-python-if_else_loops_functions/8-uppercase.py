#!/usr/bin/python3
# Graham S. Paul (8-uppercase.py)

def uppercase(str):
    """Pull string in uppercase"""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - ord('a') + ord('A'))
        print('{:s}'.format(i), end='')
    print('{}'.format(''))
