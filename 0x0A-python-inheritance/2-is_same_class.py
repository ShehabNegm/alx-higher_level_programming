#!/usr/bin/python3
"""define a function to return if object is part of class"""


def is_same_class(obj, a_class):
    """return True if obj is instance of a_class"""

    if type(obj) is a_class:
        return True
    else:
        return False
