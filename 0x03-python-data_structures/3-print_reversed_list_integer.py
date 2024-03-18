#!/usr/bin/python3
# Hamud001


def print_reversed_list_integer(my_list=[]):
    """function that prints all integer in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
