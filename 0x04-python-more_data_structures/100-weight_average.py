#!/usr/bin/python3
def weight_average(my_list=[]):
    """function to return weighted average"""

    if my_list == []:
        return 0

    else:
        multi = 0
        sub = 0

        for i in my_list:
            multi += i[0] * i[1]
            sub += i[1]

        return multi / sub
