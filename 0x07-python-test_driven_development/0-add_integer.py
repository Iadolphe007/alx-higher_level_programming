#!/usr/bin/python3
"""
this function add two integers
 Returns:
     sum of two integers
"""


def add_integer(a, b=98):

    """ check if a and b are float"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    sum = a + b
    return sum
