#!/usr/bin/python3
"""module to instantiate subclass MyList."""


class MyList(list):
    """class inherits from list."""

    def print_sorted(self):
        """prints the list, but sorted(ascending sort)."""
        print(sorted(self))
