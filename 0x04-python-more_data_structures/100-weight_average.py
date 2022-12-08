#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    denom = 0
    numer = 0
    for x, y in my_list:
        numer += (x * y)
        denom += y
    result = numer / denom
    return result
