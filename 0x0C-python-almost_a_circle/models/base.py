#!/usr/bin/python3
# base.py
"""class base"""
import json


class Base:
    """class base"""

    __nb_objects = 0  # object id

    def __init__(self, id=None):
        """class initialization"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list of dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
