#!/usr/bin/python3
"""function which find the peak value """


def find_peak(list_of_integers):
    """function which find the peak value """
    lst = list_of_integers
    if not lst:
        return None
    #if lst[0] >= lst[1]:
     #   return lst[0]
    for i in range(len(lst) -1):
        if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
            return lst[i]
    if lst[i - 1] >= lst[i - 2]:
        return lst[i -1]
