#!/usr/bin/python3
# Graham S. Paul (1-my_list.py)
"""
Holds class MyList
"""


class MyList(list):
    """
    Assusmed from list
    """
    def print_sorted(self):
        """Pulls list of ints all sorted in arising structure"""
        print(sorted(self))
