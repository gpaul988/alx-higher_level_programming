#!/usr/bin/python3
# Graham S. Paul (4-from_json_string.py)
"""
Restores python data shape from JSON string
"""


def from_json_string(my_str):
    """
    Restores python data shape from JSON string
    """
    import json

    return json.loads(my_str)
