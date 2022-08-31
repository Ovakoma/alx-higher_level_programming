#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for k in sorted_dict:
        print("{:s}: {:s}".format(k, str(a_dictionary[k])))
