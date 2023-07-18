#!/usr/bin/python3
"""square class"""
from models.rectangle import rectangle


class square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        str_s = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)
         return str_s + str_id + str_xy + str_w
