#!/usr/bin/python3
"""define a class student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """class instanation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary rep. of class"""
        return self.__dict__
