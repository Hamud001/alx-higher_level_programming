#!/usr/bin/python3
# Hamud001


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    response = [num if num != search else replace for num in my_list]
    return response
