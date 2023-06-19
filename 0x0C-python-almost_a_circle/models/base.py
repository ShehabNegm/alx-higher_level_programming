#!/usr/bin/python3
# base.py
"""class base"""
import json
import os.path
import csv


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

        if dictionary and dictionary != {}:

            if cls.__name__ == "Rectangle":
                r = cls(1, 1)
            else:
                r = cls(1)
            r.update(**dictionary)
            return r

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = "./" + cls.__name__ + ".json"

        if not os.path.isfile(filename):
            return []

        else:
            filename = cls.__name__ + ".json"

            with open(filename, "r") as f:
                list_string = f.read()

            L = Base.from_json_string(list_string)
            L_inst = [cls.create(**i) for i in L]
            return L_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:

            if list_objs is None:
                f.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]

                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]

                w = csv.DictWriter(f, fieldnames=fields)
                for i in list_objs:
                    w.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""

        filename = "./" + cls.__name__ + ".csv"

        if not os.path.isfile(filename):
            return []

        else:
            filename = cls.__name__ + ".csv"

            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]

                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]

                L = csv.DictReader(f, fieldnames=fields)
                L = [dict([k, int(v)] for k, v in d.items())
                     for d in L]
                return [cls.create(**i) for i in L]
