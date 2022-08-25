#!/usr/bin/python3
from sys import argv
def main():
    num_args = len(argv) - 1
    if (num_args < 1):
        print("{} arguments.".format(num_args))
    elif (num_args == 1):
        print("{} argument:\n{}: {}".format(num_args, num_args, argv[1]))
    elif (num_args > 1):
        for i in range(1, len(argv))
        print("{} arguments:\n{}: {}".format(num_args, num_args, argv[i]))

if __name__ == "__main__":
    main()
