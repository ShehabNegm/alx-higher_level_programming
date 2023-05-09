#!/usr/bin/python3
def fizzbuzz():
    """function to print Fizz if number is multiplied by 3
    Buzz if number multiplied by 5 and FizzBuzz if both"""

    for i in range(1, 101):
        if i % 3 == 0 and i % 15 != 0:
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0 and i % 15 != 0:
            print("{}".format("Buzz"), end=" ")
        elif i % 15 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{}".format(i), end=" ")
