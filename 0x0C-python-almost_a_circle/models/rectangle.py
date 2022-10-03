#!/usr/bin/python3
"""module contains Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """class inherits from Base class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class construction with public instances.
        Args:
            width: width of rectangle
            height: height of rectangle
            x: coordinate
            y: coordinate
            id: inherited from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter method for width attr."""
            return self.__width

        @width.setter
        def width(self, value):
            """setter method for width attr."""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """getter method for height attr."""
            return self.__height

        @height.setter
        def height(self, value):
            """setter method for height attr."""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """getter method for x attr."""
            return self.__x

        @x.setter
        def x(self, value):
            """setter method for x attr."""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be > 0")
            self.__x = value

        @property
        def y(self):
            """getter method for y attr."""
            return self.__y

        @y.setter
        def y(self, value):
            """setter method for y attr."""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be > 0")
            self.__y = value

        def area(self):
            """returns the area of the Rectangle instance."""
            return self.width * self.height

        def display(self):
            """prints in stdout the Rectangle instance with the
            character #"""
            [print("") for i in range(self.__y)]
            for r in range(self.__height):
                print(" " * self.__x, end='')
                for c in range(self.__width):
                    print("#", end='')

        def __str__(self):
            """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
            return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                    type(self).__name__, self.id, self.__x,
                    self.__y, self.__width, self.__height))

        def update(self, *args, **kwargs):
            """assigns an argument to each attribute.
            Args:
                *args (ints): New attribute values.
                    - 1st argument represents id attribute
                    - 2nd argument represents width attribute
                    - 3rd argument represents height attribute
                    - 4th argument represents x attribute
                    - 5th argument represents y attribute
                **kwargs (dict): assigns a key/value argument to attributes
            """
            for arg in args:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

            for k, v in kwargs.items():
                argm = ["id", "width", "height", "x", "y"]
                if (k in kwargs) == argm[0]:
                    self.id = v
                elif (k in kwargs) == argm[1]:
                    self.width = v
                elif (k in kwargs) == argm[2]:
                    self.height = v
                elif (k in kwargs) == argm[3]:
                    self.x = v
                elif (k in kwargs) == argm[4]:
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {"id": self.id,
                "width": self. width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
