#!/usr/bin/python3
"""defining class"""


class MyInt(int):
    """invert int operator"""
    def __eq__(self, value):
        """override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
