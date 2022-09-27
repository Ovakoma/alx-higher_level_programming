#!/usr/bin/python3
"""module contains function that appends string
at the end of file."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added.
    """
    with open(filename, mode='a', encoding='UTF-8') as file:
        nb_char = file.write(text)
    return nb_char
