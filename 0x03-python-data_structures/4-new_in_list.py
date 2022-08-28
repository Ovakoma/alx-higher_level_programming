#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_cpy = my_list.copy()
    if idx < 0:
        return my_cpy
    elif idx > len(my_cpy) - 1:
        return my_cpy
    else:
        my_cpy[idx] = element
        return my_cpy
