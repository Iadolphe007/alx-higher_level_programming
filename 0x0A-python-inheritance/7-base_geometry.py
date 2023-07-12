#!/usr/bin/python3
""" Base geometry class"""


class BaseGeometry:
    """this is a base geometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valid value to integer"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
