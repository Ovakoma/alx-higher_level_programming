#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listlen = len(my_list) - 1
    for elem in range(listlen + 1):
        print("{:d}".format(my_list[listlen]))
        listlen -= 1
