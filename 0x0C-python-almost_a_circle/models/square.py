#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inheirt from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialise square property"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """special string method"""
        str_s = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)

        return str_s + str_id + str_xy + str_w

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """settingsize"""
        self.width = value
        self.height = value

    def __str__(self):
        """special str """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)
        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """update model"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """change to dictionary model"""
        list_atr = ['id', 'size', 'x', 'y']
        dict_re = {}

        for key in list_atr:
            if key == 'size':
                dict_re[key] = getattr(self, 'width')
            else:
                dict_re[key] = getattr(self, key)
        return dict_re
