#!/usr/bin/python3
from sys import argv
def main():
    added = 0
    for i in range(1, len(argv)):
        added += int(argv[i])
    print('{}'.format(added))

if __name__ == "__main__":
    main()
