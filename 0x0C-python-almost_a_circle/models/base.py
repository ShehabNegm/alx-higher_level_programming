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
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:

            if list_objs is None:
                f.write("[]")

            else:
                L = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(L))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        r = cls(1, 2, 3, 4)
        r.update(**dictionary)
        return r
