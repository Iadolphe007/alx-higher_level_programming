#!/usr/bin/python3
""" Base geometry class"""


class BaseGeometry:
    """this is a base geometry class"""
    def area(self):
        """check area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
