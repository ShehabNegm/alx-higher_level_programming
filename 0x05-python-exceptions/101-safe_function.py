#!/usr/bin/python3
def safe_function(fct, *args):
    """ safly execute function"""
    import sys

    try:
        return fct(*args)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
        return None
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
        return None
