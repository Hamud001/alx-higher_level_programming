#!/usr/bin/python3
# Hamud001


def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [n for n in my_list]
    copy[idx] = element
    return (copy)
