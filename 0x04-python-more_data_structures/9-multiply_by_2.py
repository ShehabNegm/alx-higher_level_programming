def multiply_by_2(a_dictionary):
    """function to return items of dict multiplyed by 2"""

    d = {}
    for k in a_dictionary.keys():
        d[k] = (a_dictionary[k]) * 2

    return d
