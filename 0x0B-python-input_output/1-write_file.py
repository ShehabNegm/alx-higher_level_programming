#!/usr/bin/python3
"""define function to write to file"""


def write_file(filename="", text=""):
    """function to overwrtite a filename after opening it"""

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(str(text))
