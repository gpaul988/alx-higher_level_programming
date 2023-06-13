#!/usr/bin/python3
# Graham S. Paul (8-multiple_returns.py)
def multiple_returns(sentence):
    """Reverses length of string and its begining character"""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
