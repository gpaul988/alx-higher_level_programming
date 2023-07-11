#!/usr/bin/python3
# Graham S. Paul (3-to_json_string.py)
"""
Restores JSON constitution of obj (string)
"""


def to_json_string(my_obj):
    """
    Restores JSON constitution of obj (string)
    """
    import json

    return json.dumps(my_obj)
