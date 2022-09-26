#!/usr/bin/python3
"""module to initialize lookup(...) function."""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object."""
    return dir(obj)
