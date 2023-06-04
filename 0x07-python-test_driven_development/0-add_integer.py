#!/usr/bin/python3
# 0-add_integer.py
""" define python function """


def add_integer(a, b=98):
    """function to add two integers
    Args:
        a (int) : if not int or float raise TypeError
        b (int) : if not int or float raise TypeError
    Return:
        will return addition to a and b as an int
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
