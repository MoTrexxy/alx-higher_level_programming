#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    flag_list = my_list[:]
    for count, m in enumerate(my_list):
        if m % 2 == 0:
            flag_list[count] = True
        else:
            flag_list[count] = False
    return(flag_list)
