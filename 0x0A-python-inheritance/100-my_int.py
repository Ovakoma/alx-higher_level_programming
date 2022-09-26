#!/usr/bin/python3
"""module contains MyInt class."""


class MyInt(int):
    """class inherits from int data type class."""

    def __eq__(self, value):
        """Works inversely to int operator."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Works inversely to the != operator."""
        return super().__eq__(value)
