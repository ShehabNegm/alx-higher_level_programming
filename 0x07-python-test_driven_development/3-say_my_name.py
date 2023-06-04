#!/usr/bin/python3
# 3-say_my_name.py
""" define function to print name"""


def say_my_name(first_name, last_name=""):
    """function will print the last name and first name

    Args:
        first_name (str) : must be string
        last_name (str) : must be string or empty

    Return:
        will print the name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
