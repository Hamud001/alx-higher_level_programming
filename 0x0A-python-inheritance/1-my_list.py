#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """represents my list"""
    def __init__(self):
        """initializes it"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
