#!/usr/bin/python3
# Hamud001


def print_sorted_dictionary(a_dictionary):
    """function that print a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(key, a_dictionary[key]))
