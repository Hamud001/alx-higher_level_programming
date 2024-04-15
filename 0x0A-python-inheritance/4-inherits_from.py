#!/usr/bin/python3
"""an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks for inherited instance of a class.

    Args:
        obj (any): The object.
        a_class (type): The class to match obj.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
