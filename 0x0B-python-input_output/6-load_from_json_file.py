#!/usr/bin/python3
"""function that create an obj from json file"""
import json


def load_from_json_file(filename):
    """ function that create an obj from json file"""

    with open(filename) as f:
        x = json.load(f)
    return x
