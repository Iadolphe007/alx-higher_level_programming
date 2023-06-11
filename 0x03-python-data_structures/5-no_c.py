#!/usr/bin/python3
def no_c(my_string):
    new_string = [char for char in my_string if char != "c" and char != "C"]
    no_c = "".join(new_string)
    return no_c
