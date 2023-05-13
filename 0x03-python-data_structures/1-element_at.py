#!/usr/bin/python3
def element_at(my_list, idx):
    """function to return the element at index idx of a list"""

    if idx < 0 or idx >= len(my_list):
        return None

    else:
        return my_list[idx]
