#!/usr/bin/python3
# Graham S. Paul (100-my_int.py)
"""
Holds class MyInt that is assumed from int
"""


class MyInt(int):
    """
    Procedure:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        """Assumes num"""
        self.num = num

    def __eq__(self, other):
        """
        Retrieves:
           execute if both not same
        """
        return self.num != other

    def __ne__(self, other):
        """
        Retrieves:
           execute if both same
        """
        return self.num == other
