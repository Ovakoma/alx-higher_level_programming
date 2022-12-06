#!/usr/bin/python3


def main(argv):
    n_arg = len(argv) - 1
    if (n_arg < 1):
        print("{} arguments.".format(n_arg))
    elif (n_arg == 1):
        print("{} argument:".format(n_arg))
        print("{}: ".format(n_arg) + argv[1])
    elif (n_arg > 1):
        print("{} arguments:".format(n_arg))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))


if __name__ == "__main__":
    import sys
    main(sys.argv)
