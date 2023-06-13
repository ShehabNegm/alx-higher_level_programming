#!/usr/bin/python3
"""function to returns the dictionary description for JSON"""


def class_to_json(obj):
    """function to return json rep of an object"""

    return obj.__dict__
