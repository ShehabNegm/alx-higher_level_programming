#!/usr/bin/python3
"""script that adds all arguments to a Python list & save them to a file"""
import json
from sys import argv


if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_list = []
    items_list += argv[1:]
    save_to_json_file(items_list, "add_item.json")
