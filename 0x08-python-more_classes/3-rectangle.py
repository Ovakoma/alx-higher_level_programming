#!/usr/bin/python3
"""class defines a rectangle."""

class Rectangle:
    '''defines rectangle based on 1-rectangle.py'''
    def __init__(self, width=0, height=0):
        '''instance to initialize attributes.
        Args:
            width: private instance attribute.
            height: private instance attribute.
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    """Retrieves the value of height."""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
            """returns the perimeter of rectangle"""
            if (self.__width == 0 or self.__height == 0):
                return 0
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect = []
        for h in range(self.__height):
            for w in range(self.__width):
                rect.append("#")
            if h != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

