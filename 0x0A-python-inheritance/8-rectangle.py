#!/usr/bin/python3
""" base geometry import"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class that inherit from BaseGeometry"""
    def __init__(self, width, height):
        """Rectangle initiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__heigth = height
