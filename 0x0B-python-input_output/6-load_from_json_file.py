#!/usr/bin/python3
"""module contains function that creates an Object from JSON file."""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'."""
    with open(filename, 'r', encoding='utf-8') as file:
        json_obj = json.load(file)
    return json_obj
