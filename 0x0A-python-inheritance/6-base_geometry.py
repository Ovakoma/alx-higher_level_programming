#!/usr/bin/python3
"""module instantiates area(...) function."""


class BaseGeometry:
    """class contains public instance method."""
    def area(self):
        """raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
