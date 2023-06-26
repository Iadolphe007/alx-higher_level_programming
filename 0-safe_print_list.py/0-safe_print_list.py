#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            new_list = my_list[i]
        except IndexError: ('list index out of range')
        except TypeError: ('list indices must be integers or slices, not float')
        return new_list
