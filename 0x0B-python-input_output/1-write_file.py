#!/usr/bin/python3
"""module contains function that writes to text file."""


def write_file(filename="", text=""):
    """function writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        nb_char = file.write(text)
    return nb_char
