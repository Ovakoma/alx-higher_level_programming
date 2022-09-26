#!/usr/bin/python3
"""module defines class and subclass."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle class."""

    def __init__(self, size):
        """instantiation with size.
        Args:
            size(int): size of square.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implements area function."""
        return self.__size ** 2
