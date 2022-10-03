#!/usr/bin/python3
"""module contains unittest cases."""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from turtle import position
from io import StringIO
from unittest.mock import patch

import os
import unittest


class TestBaseInstances(unittest.TestCase):
    """class contains methods to conduct possible test cases
    for the base.py function."""

    def setUp(self):
        """set up function for models/base.py module."""
        self.shape = Base()
        self.shape_1 = Base(12)
        self.shape_2 = Base()
        self.shape_3 = Base()
        self.shape_4 = Base(None)

    def test_peculiarbaseinstance(self):
        """base objects of same id are not the same."""
        self.assertFalse(self.shape is self.shape_1)

    def test_increament(self):
        """test that test objs without arg increase by 1."""
        self.assertEqual(self.shape_2.id - self.shape.id,
                        self.shape_4.id - self.shape_3.id)
        self.assertTrue((self.shape_2.id - self.shape.id) == 1)

    def test_multiple_arg(self):
        """if more than one argument is passed to function"""
        with self.assertRaises(TypeError):
            Base(2, 1)

    def test_bool_arg(self):
        """test if arg is boolean."""
        b = Base(True)
        self.assertEqual(b.id, True)
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_raisenb_obj(self):
        """test for private class attribute __nb_objects."""
        with self.assertRaises(AttributeError):
            self.shape.__nb_objects += 1

    def test_str_id(self):
        self.assertEqual(Base("sorry").id, "sorry")

    def test_list_arg(self):
        b = Base(["buy"])
        self.assertIsInstance(b.id, list)

    def test_float_arg(self):
        b = Base(5.2)
        self.assertIsInstance(b.id, float)


class TestBaseToStr(unittest.TestCase):
    """class contains test case for json related methods of Base class"""
    def test_to_json_str(self):
        r = Rectangle(10, 7, 2, 8)
        with self.assertRaises(TypeError):
            Base.to_json_string()
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(str, type(Base.to_json_string(
                        [r.to_dictionary()])))
        self.assertEqual(Base.to_json_string([{}]), '[{}]')
        self.assertEqual(Base.to_json_string([{"len": 2}]),
                        '[{"len": 2}]')

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        square_json_input = Square.to_json_string(list_input)
        square_output = Square.from_json_string(square_json_input)
        self.assertEqual(list, type(list_output))
        self.assertEqual(list_input, list_output)
        self.assertEqual(list_input, square_output)
        self.assertEqual([], Base.from_json_string(None))
        with self.assertRaises(TypeError):
            Base.from_json_string()
        with self.assertRaises(TypeError):
            Base.from_json_string([], 6)

class TestRectangleInstancesandAttributes(unittest.TestCase):
    """class contains test suite for Rectangle instances and attributes."""
    def test_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_no_arg_is_passed(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_error_raised_when_one_arg_is_passed(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_kwarg(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r1.width = 10
        r1.height = 2
        self.assertEqual(10, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(r2.id - r1.id, 1)
        self.assertEqual(r3.id, 12)

    def test_error_if_width_not_int(self):
        with self.assertRaises(TypeError):
            r = Rectangle(3.4, 4)

    def test_raise_error_if_arg_is_str(self):
        with self.assertRaises(TypeError):
            Rectangle(3, "7")

    def test_error_if_x_is_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, True)

    def test_error_if_y_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 2, 4, "f")

    def test_width_less_than_equal_to_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_height_lessorequalto_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(8, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(3, -4)

    def test_x_lessthanequalto_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 2, -4)

    def test_y_lessthanqualto_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, y=-2)
        with self.assertRaises(ValueError):
            r = Rectangle(2, 4, y=-1)

class TestPolygonMethods(unittest.TestCase):
    """class contains test suite for Rectangle methods"""
    
    @classmethod
    def tearDown(self):
        """delete all created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_rectangle_area(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 12)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file2(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_square_save(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue("[Rectangle] (1) 1/0 - 3/5", r1)
        self.assertTrue("[Rectangle] (1) 1/0 - 3/5", r2)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))
        self.assertTrue(all(type(obj) == Rectangle for obj in
                        list_rectangles_output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_string(self):
        self.r1 = Rectangle(3, 2)
        string = str(self.r1)

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(self.r1, end="")
            self.assertEqual(fake_stdout.getvalue(), string)

    def test_update(self):
        self.r1 = Rectangle(3, 2)
        self.r1.update(23, 2, 3, 4)

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(self.r1, end="")
            self.assertEqual(fake_stdout.getvalue(), str(self.r1))

        self.r1.update()
        self.assertEqual(self.r1.to_dictionary(),
        {"id": 23, "width": 2, "height": 3, "x": 4, "y": 0})
        self.r1.update(89)
        self.assertEqual(self.r1.to_dictionary(),
        {"id": 89, "width": 2, "height": 3, "x": 4, "y": 0})

class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))
