#!/usr/bin/python3
"""define function to appened to file"""


def append_write(filename="", text=""):
    """function to appened to a filename after opening it"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(str(text))
