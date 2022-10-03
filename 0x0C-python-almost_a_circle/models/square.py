#!/usr/bin/python3
"""module contains Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """class constructor with public instances.
        Args:
            size: size of square
            x: inherited from Rectangle
            y: inherited
            id: inherited
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width))

    def update(self, *args, **kwargs):
        """public method assigns attriubtes:
        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
            **kwargs can be thought of as a double pointer to a
            dictionary: key/value (keyworded arguments)
        """
        attr = ["id", "size", "x", "y"]
        for k, v in zip(attr, args):
            setattr(self, k, v)
        if type(args) is None or len(args) == 0 and type(kwargs) is dict:
            for k, v in kwargs.items():
                if k in attr:
                    setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
