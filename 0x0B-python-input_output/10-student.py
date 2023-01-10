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
                    attr[k] = self.__dict__[k]
            return attr
        return self.__dict__
