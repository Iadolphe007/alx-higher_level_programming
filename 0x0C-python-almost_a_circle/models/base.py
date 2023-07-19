#!/usr/bin/python3
"""class base"""
import json


class Base:
    """base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == '[]':
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = '{}.json'.format(cls.__name__)
        with open(filename, "w") as file:
            if list_objs is None:
                file.write('[]')
            else:
                list_dic = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dic))
