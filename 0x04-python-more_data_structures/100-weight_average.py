#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    res = 0
    res2 = 0
    for m, n in my_list:
        res += m * n
        res2 += n
    return (res / res2)
