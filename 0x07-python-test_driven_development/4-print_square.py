#!/usr/bin/python3
""" Function print square """


def print_square(size):
    """
    Function which print square with characteer #
    Args:
        size: size of square
    Raises:
        TypeError: if the size is not interger
        ValueError: if the size is less than 0
        TypeError: wheb sixe is a float and less than 0
    Return:
        square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
