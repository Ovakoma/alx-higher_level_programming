#!/usr/bin/python3
"""module contains Base class."""
import json
import pickle
import csv


class Base:
    """this class serves as the 'base' of all other classes."""
    
    __nb_objects = 0
    """private class attribute."""
    
    def __init__(self, id=None):
        """instantiation of class constructor with instance attr.
        Arg:
            id(int): public instance attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries.
        Arg:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
        Arg:
            list_objs: list of instances which inherits of Base
        """
        filename = cls.__name__ + ".json"
        obj = to_json_string(list_objs)
        with open(filename) as jf:
            jf.write(obj)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.
        Arg:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Arg:
            **dictionary: can be thought of as a double pointer to
            a dictionary
        """
        dummy = {
                'Rectangle': (1, 3, 0, 0),
                'Square': (2, 4, 5, 61)
        }
        if cls.__name__ in dummy.keys():
            dummy = cls(*dummy[cls.__name])
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding='utf-8') as file:
                list_inst = cls.from_json_string(file.read)
                return [cls.create(**d) for k in list_inst]
        except IOError:
            return []

    @staticmethod
    def buildext(c):
        """builds the extention for csv based on class."""
        if c.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        return ["id", "size", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV.
        Arg:
            list_objs: list of instnaces which inherit from Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', encoding='utf-8') as file:
            if not list_objs:
                file.write("[]")
            writer = csv.DictWriter(file, fieldnames=cls.buildext(cls))
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, encoding='utf-8') as f:
                reader = csv.DictReader(f, fieldnames=cls.buildext(cls))
                list_dict = [dict((k, int(v)) for k, v in d.items())
                            for d in reader]
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []
