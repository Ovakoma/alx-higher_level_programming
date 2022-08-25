#!/usr/bin/python3
from sys import argv
def main():
    n_arg = len(argv) - 1
    if (n_arg < 1):
        print("{} arguments.".format(n_arg))
    elif (n_arg == 1):
        print("{} argument:\n{}: {}".format(n_arg, n_arg, argv[1]))
    elif (n_arg > 1):
        print("{} arguments:".format(n_arg))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))

if __name__ == "__main__":
    main()
