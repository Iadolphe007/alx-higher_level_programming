#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_el = set(set_1 ^ set_2)
    return diff_el
