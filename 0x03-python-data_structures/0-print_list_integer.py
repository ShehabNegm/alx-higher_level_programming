#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """function to print integers of a list each per line"""

    if my_list == []:
        return None

    else:
        for i in my_list:
            print("{:d}".format(i))
