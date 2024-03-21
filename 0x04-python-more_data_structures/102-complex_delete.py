#!/usr/bin/python3
# Hamud001


def complex_delete(a_dictionary, value):
    """function delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for i, n in a_dictionary.items():
            if n == value:
                del a_dictionary[i]
                break

    return (a_dictionary)
