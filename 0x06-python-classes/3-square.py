#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """A class that represents a square.
    Private instance attribute: size.
    Instantiation with optional size.
    Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """Initialising this square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
