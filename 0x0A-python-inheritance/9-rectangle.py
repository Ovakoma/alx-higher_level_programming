#!/usr/bin/python3
"""module contains class and subclass."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherits from BaseGeometry class."""

    def __init__(self, width, height):
        """instantiation with width and height.
        Args:
            width(int): width of Rectangle.
            height(int): height of Rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

        def area(self):
            """implements area function."""
            return (self.__width * self.__height)

        def __str__(self):
            """returns rectangle description of object."""
            return ("[{}] {:d}/{:d}".format(self.__class__.__name__,
                    self.__width, self.__height))
