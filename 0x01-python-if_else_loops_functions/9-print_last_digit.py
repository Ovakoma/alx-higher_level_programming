#!/usr/bin/pyhton3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    last_num = no % 10
    print("{}".format(last_num), end='')
    return last_num
