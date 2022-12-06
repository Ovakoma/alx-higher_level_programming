#!/usr/bin/python3
def main():
    for name in dir(hide):
        if not (name[0] == "_" and name[1] == "_"):
            print(name)


if __name__ == "__main__":
    import hidden_4 as hide
    main()
