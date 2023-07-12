#!/usr/bin/python3
""" class of Mylist taht inherit from List"""


class MyList(list):
    """ class taht inherit from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
