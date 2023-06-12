#!/usr/bin/python3
"""function to checl if obj is part of class"""


def inherits_from(obj, a_class):
    """return True is obj is part of class, False otherwise"""

    return isinstance(obj, a_class) and type(obj) != a_class
