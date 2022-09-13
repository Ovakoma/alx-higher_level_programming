#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ class that defines a square with private
    instance attribute: size. """

    def __init__(self, size=0):
        """ Initialize square.

        Args:
            size(int): Size of square.
        """
        self.__size = size
