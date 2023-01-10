#!/usr/bin/python3
"""module contains a Student class"""


class Student:
    """class defines a student object"""
    def __init__(self, first_name, last_name, age):
        """instantiation of public instance attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all(type(el) is str for el in attrs):
            attr = {}

            for k in attrs:
                if k in self.__dict__:
                    attr[k] = self.__dict__[key]
            return attr
        return self.__dict__

    def reload_from_json(self, json):
        """public method replaces all attributes of the Student instance
        Args:
            json: assumed to be a dictionary.
        """
        for k, v in json.items():
            setattr(self, k, v)
