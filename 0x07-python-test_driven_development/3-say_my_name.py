#!/usr/bin/python3
""" function print the name """


def say_my_name(first_name, last_name=""):
    """
    function which print the name

    Args:
        first_name: string of name
        last_name: last name of the string
    Raises:
        TypeError: if the first name and the last name are not string
    Returns:
        first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
