#!/usr/bin/python3
"""function to save json representation of obj to file"""
import json


def save_to_json_file(my_obj, filename):
    """function to write json repre. of obj to file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
