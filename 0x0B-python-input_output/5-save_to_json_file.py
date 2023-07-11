#!/usr/bin/python3
# Graham S. Paul (5-save_to_json_file.py)
"""
Notes Python obj to file using JSON constitution
"""


def save_to_json_file(my_obj, filename):
    """
    Writes Python obj to file using JSON represenation
        """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
