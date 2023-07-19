#!/usr/bin/python3
"""class base"""
import json
import os.path
import csv


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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(10, 10)
            else:
                new = cls(10)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
         """Serializes list_objs and saves to file"""
         filename = cls.__name__ + ".csv"
         with open(filename, "w", newline="") as csvfile:
             if list_objs is None or list_objs == []:
                 csvfile.write("[]")
             else:
                 if cls.__name__ == "Rectangle":
                     fieldnames = ["id", "width", "height", "x", "y"]
                 else:
                     fieldnames = ["id", "size", "x", "y"]
                     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                     for obj in list_objs:
                         writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
