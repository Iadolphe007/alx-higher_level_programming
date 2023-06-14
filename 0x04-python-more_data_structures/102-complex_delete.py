#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delet_key = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            deket_key.append(key)

    for key in delet_key:
        del a_dictionary[key]

    return a_dictionary
