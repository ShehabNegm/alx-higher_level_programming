#!/usr/bin/python3
def no_c(my_string):
    """function to remove c and C from any string given"""

    new_string = ""

    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i

    return new_string
