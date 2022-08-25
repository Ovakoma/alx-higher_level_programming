#!/usr/bin/python3
from calculator_1 import add sub div mul
def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(10, 5)))

if __name__ == "__main__":
    main()

def submain():
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(10, 5)))

if __name__ == "__main__":
    submain()

def mulmain():
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, mul(10, 5)))

if __name__ == "__main__":
    mulmain()

def divmain():
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, div(10, 5)))

if __name__ == "__main__":
    divmain()
