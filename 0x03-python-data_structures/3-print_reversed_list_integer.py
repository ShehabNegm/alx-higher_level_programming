#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print a given list in reverse"""
    if my_list == []:
        return None

    else:
        for i in range(len(my_list) - 1, -1, -1):
            print("{}".format(my_list[i]))
