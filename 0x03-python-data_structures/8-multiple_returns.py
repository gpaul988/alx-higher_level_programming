#!/usr/bin/python3
# Graham S. Paul (8-multiple_returns.py)

"""Reverses length of string and its begining character"""

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
