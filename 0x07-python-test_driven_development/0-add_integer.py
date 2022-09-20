#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns integer addition of a and b

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If a or b is not a float or integer.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
