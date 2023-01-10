#!/usr/bin/python3
"""module contains function that returns description with the
simple data structure."""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.
    """
    return obj.__dict__
