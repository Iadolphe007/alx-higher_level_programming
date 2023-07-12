#!/usr/bin/python3
"""check for instance of class"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        returns true if the object is exactly the instance of the class
    """
    return type(obj) is a_class
