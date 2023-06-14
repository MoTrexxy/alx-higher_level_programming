#!/usr/bin/python3
def complex_delete(my_dict, value):
    targets = []
    for key, key_value in my_dict.items():
        if key_value is value:
            targets.append(key)
    for m in targets:
        del my_dict[m]
    return(my_dict)
