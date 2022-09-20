#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest
max_integer = __import__("6-max_integer").max_integer

class MaxIntTestCase(unittest.TestCase):
    def test_empty_list(self):
        """tests if lists is empty."""
        self.assertEqual(max_integer([]), None)

    def test_list_of_integers(self):
        """tests for list of integers"""
        i = [1, 2, 4]
        self.assertTrue(max_integer([i]))

    def test_single_list_element(self):
        """tests if list comprises of single element"""
        s = [2]
        self.assertEqual(max_integer([s]), s[0])

    def test_max_at_beginning(self):
        """checks if max int is at the beginning of list"""
        b = [8, 2, 3, 5]
        self.assertEqual(max_integer([b]), b[0])

    def test_float(self):
        """checks for max in floats"""
        f = [2.3, 5.6, 1.2, 3.4]
        self.assertEqual(max_integer([f]), 5.6)

    def test_int_float(self):
        """checks for max value in list of integers and floats"""
        if = [4, 2.34, 40]
        self.assertEqual(max_integer([if]), 40)

    def test_large_list(self):
        """Tests a list that is large"""
        large_list = list(range(2, 10000, 3)) + list(range(3000, 100, -2))
        self.assertEqual(max_integer(large_list), max(large_list))

    def test_string(self):
        """Tests a string"""
        string = "Holberton School"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """Tests a list of strings"""
        list_of_strings = ["holberton", "school", "software", "engineering"]
        self.assertEqual(max_integer(list_of_strings), 'software')

if __name__ == "__main__":
    unittest.main()
