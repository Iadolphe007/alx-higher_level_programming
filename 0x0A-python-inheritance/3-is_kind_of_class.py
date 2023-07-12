#!/usr/bin/python3
"""check for instance of the object"""


def is_kind_of_class(obj, a_class):
    """
    check instance of, or if the object is an instance of
    a class that inherited from
    Args:
        obj: object to check for
        a_class: class to check into
    Returns:
        returnstrue of it belongs to it otherwise False
    """
    return isinstance(obj, a_class)
