#!/usr/bin/python3
class Square:
    """ class defines square """
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """ retrieve current size of square """
        return self.size

    @size.setter
    def size(self, val):
        """ sets size value of sqaure """
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
