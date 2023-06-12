#!/usr/bin/python3
def lookup(obj):
    """function to return list of available methods and arrtibutes of an obj"""
    if obj:
        return dir(obj)
