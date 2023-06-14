#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_key = list(a_dictionary.keys())
    sort_key.sort()
    for i in sort_key:
         print("{}: {}".format(i, a_dictionary.get(i)))
