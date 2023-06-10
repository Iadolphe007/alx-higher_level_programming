#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if isinstance(i, int):
            print("{}".format(i))

