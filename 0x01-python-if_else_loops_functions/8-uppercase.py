#!/usr/bin/python3
def uppercase(str):
    casechange = 32
    sstr = ""
    for letter in str:
        if ord('a') <= ord('i') <= ord('z'):
            casechange = 32
            cap = chr(ord(i) - casechange)
        else:
            casechange = 0
            cap = letter
        sstr = sstr + t
    print("{}".format(sstr))