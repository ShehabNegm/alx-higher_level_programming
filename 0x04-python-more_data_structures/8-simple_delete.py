#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """function to delete from a dictionary"""

    if key and key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary
