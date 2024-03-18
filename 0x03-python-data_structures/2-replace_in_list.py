#!/usr/bin/python3
# Hamud001


def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
