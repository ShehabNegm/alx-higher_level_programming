#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function to return list of True if number is divisble by 2 """

    if my_list:
        return [True if i % 2 == 0 else False for i in my_list]
