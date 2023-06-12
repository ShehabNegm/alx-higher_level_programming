#!/usr/bin/python3
"""function to check if obj is part of class or parent class"""


def is_kind_of_class(obj, a_class):
    """return true if obj is instance of a class"""

    return isinstance(obj, a_class)
