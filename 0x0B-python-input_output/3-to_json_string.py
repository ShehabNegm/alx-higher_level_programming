#!/usr/bin/python3
"""function to return the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function to serializing an obj"""

    return json.dumps(my_obj)
