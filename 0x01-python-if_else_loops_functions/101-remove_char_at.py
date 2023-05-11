#!/usr/bin/python3
def remove_char_at(str, n):

    """function to remove n char from string and return a copy"""

    copy = ""

    for i in range(len(str)):

        if i != n:
            copy += str[i]

    return copy
