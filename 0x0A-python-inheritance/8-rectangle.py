#!/usr/bin/python3
"""module contains subclass Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry."""

    def __init__(self, width, height):
        """instantiation with width and height.
        Args:
            width(int): width of rectangle.
            height(int): height of rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
