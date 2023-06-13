#!/usr/bin/python3
"""function to return the object from json i.e deserializing"""
import json


def from_json_string(my_str):
    """function to deserializing json object"""

    return json.loads(my_str)
