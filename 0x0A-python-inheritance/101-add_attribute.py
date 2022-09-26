#!/usr/bin/python3
"""module contains function that adds new attribute."""


def add_attribute(obj, name, value):
    """function adds mew attribute to an object if it's possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
