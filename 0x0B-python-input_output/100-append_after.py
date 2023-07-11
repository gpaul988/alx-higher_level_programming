#!/usr/bin/python3
# Graham S. Paul (100-append_after.py)
"""
Attach str after lines that adds keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Attach str after lines that add keyword (search_string)
    """

    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
