#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """function to retutn a tuple of sum of 2 tuples"""

    La = [0, 0]
    Lb = [0, 0]

    if len(tuple_a) == 1:
        La[0] = tuple_a[0]

    if len(tuple_a) >= 2:
        La[0] = tuple_a[0]
        La[1] = tuple_a[1]

    if len(tuple_b) == 1:
        Lb[0] = tuple_b[0]

    if len(tuple_b) >= 2:
        Lb[0] = tuple_b[0]
        Lb[1] = tuple_b[1]

    return (La[0] + Lb[0], La[1] + Lb[1])
