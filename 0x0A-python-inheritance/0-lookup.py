#!/usr/bin/python3
"""define funtion to return a list of available methods and arrtibutes"""


def lookup(obj):
    """function to return list of available methods and arrtibutes of an obj"""
    if obj:
        return dir(obj)
