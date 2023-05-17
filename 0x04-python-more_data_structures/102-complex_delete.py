#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """function to delete a key of a dictionary using its value"""

    if not value:
        return a_dictionary

    else:
        keys = list(a_dictionary.keys())[:]
        for k in keys:
            if a_dictionary[k] == value:
                del a_dictionary[k]
        return a_dictionary
