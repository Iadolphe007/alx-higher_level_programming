#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_key = 0
    max_value = 0

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
        return max_key
