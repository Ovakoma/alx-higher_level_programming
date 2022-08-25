#!/usr/bin/python3
def main(argv):
    added = 0
    for i in range(1, len(argv)):
        added += int(argv[i])
    print('{}'.format(added))

if __name__ == "__main__":
    import sys
    main(sys.argv)
