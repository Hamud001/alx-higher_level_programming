#!/usr/bin/python3
"""2-is_same_class.py."""


def is_same_class(obj, a_class):
    """Check if an objectan instance of a given class.

    Args:
        obj (any): The object.
        a_class (type): The class to match obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
