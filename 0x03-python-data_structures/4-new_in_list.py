#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """modify element at copy list without the original at indey idx"""

    if my_list:

        if idx < 0 or idx >= len(my_list):
            return my_list[:]

        else:
            copy_list = my_list[:]
            copy_list[idx] = element
            return copy_list
