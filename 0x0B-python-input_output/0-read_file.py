#!/usr/bin/python3
"""module contains function that reads text files."""


def read_file(filename=""):
    """function reads text file(UTF8)."""
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end='')
