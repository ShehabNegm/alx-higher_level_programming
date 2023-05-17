#!/usr/bin/python3
def best_score(a_dictionary):
    """function to return best score in a dict"""

    if not a_dictionary:
        return None

    else:
        best_score = 0
        best_key = None
        for k, v in a_dictionary.items():
            if v > best_score:
                best_score = v
                best_key = k

        return best_key
