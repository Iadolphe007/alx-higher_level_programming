#!/usr/bin/python3
"""Define a class Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dict representation"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attrs"""
        for k, v in json.items():
            setattr(self, k, v)
