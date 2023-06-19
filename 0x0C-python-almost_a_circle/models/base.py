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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list of dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """rites the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"

        L = []
        for i in list_objs:
            L.append(i.to_dictionary())

        obj = Base.to_json_string(L)
        with open(filename, 'w') as f:
            f.write(str(obj))
