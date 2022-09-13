#!/usr/bin/python3

class Square:
    """ class defines sqaure """

    def __init__(self, size=0):
        """ Args:
                size(int): size of square 
        """
        if not isinstance(size, int):
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size