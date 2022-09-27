#!/usr/bin/python3
"""module contains class that defines a student."""


class Student:
    """class defines a student."""
    def __init__(self, first_name, last_name, age):
        """instantiation of public attributes.
        Args:
            first_name: first name of student
            last_name: last name of student
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance."""
        return self.__dict__
