#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherity from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """height setter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        self.__height = value
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

    @property
    def x(self):
        """getting y"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting x"""
        self.__x = value
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

    @property
    def y(self):
        """getting y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setting y"""
        self.__y = value
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')

    def area(self):
        """get area model"""
        return self.__width * self.__height

    def display(self):
        """display model"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """STR DUNDER METHOS """
        str_rect = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)

        return str_rect + str_id + str_xy + str_w

    def update(self, *args, **kwargs):
        """update model"""
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """change to dictinary model"""
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
