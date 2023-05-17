#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function to replace element search in my_list by replace"""

    if my_list and replace:

        return [replace if i == search else i for i in my_list]
