#!/usr/bin/python3
"""define function to read from file"""


def read_file(filename=""):
    """function to read from a filename after opening it"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
