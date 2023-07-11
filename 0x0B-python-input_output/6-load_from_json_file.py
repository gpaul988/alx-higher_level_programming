#!/usr/bin/python3
# Graham S. Paul (6-load_from_json_file.py)
"""
Develops a Python obj from JSON file
"""


def load_from_json_file(filename):
    """
    Develops a Python obj from JSON file
      """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
