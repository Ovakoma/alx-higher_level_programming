#!/usr/bin/python3
"""module contains function that writes an Object to text file."""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        f = file.write(json.dumps(my_obj))
        return f
