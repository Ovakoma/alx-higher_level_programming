#!/usr/bin/python3
"""function that prints a square."""

def print_square(size):
    """prints square with the character #.
    Args:
        size: length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
