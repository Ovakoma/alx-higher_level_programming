#!/usr/bin/python3
"""module contains function that returns JSON representation
of an object."""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of
    an object (string)."""
    return json.dumps(my_obj)
