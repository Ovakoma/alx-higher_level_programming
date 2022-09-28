#!/usr/bin/python3
"""module contains the BaseGeometry class."""


class BaseGeometry:
    """Base class of geometry objects."""

    def area(self):
        """raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """function validates the value."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
