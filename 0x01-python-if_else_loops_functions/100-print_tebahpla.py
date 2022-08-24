#!/usr/bin/python3
last = 122
while last > 96:
    check = 0
    if (last % 2 != 0):
        last -= 32
        check = 1
    print("{:s}".format(chr(last)), end="")
    if (check):
        last += 32
    last -= 1
