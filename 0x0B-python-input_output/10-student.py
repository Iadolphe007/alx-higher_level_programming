#!/usr/bin/python3
"""Define a  student class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """inititialize  stdent class
        Args:
        firstname: string type
        lastname: string type
        age: int type
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return describtion about the class"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {n: getattr(self, n) for n in attrs if hasattr(self, n)}
        return self.__dict__
