#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = []
    for k, v in a_dictionary.items():
        if v == value:
            my_list.append(k)
    for el in my_list:
        del a_dictionary[el]
    return a_dictionary
