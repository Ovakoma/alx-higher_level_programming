#!/usr/bin/python3
def no_c(my_string):
    list_str = []
    new_str = ""
    for elem in my_string:
        list_str.append(elem)
    for letter in list_str:
        if letter == 'c' or letter == 'C':
            list_str.remove(letter)
    for char in list_str:
        new_str += str(char)
    return new_str
