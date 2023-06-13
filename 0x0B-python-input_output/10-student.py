#!/usr/bin/python3
"""define a class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """class instanation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary rep. of class"""

        if type(attrs) is not list:
            return self.__dict__

        else:
            dic = {}
            if type(attrs) is list:
                for i in attrs:

                    if type(i) is not str:
                        return self.__dict__

                    else:
                        for k in self.__dict__.keys():
                            if k == i:
                                dic[i] = self.__dict__[i]
                return dic
