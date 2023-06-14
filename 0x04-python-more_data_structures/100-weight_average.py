#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for tuples in my_list:
        num += tuples[0] * tuples[1]
        den += tuples[1]
    return num / den
