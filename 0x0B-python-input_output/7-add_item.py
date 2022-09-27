#!/usr/bin/python3
"""module contains script that adds all args to a python list,
and then save them to a file"""
import sys


if __name__ = "__main__":
    l_file = __import__('6-load_from_json_file').load_from_json_file
    s_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        load = l_file("add_item.json")
    except FileNotFoundError:
        load = []
    load.extend(sys.argv[1:])
    s_file(load, "add_item.json")
