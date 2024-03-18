#!/usr/bin/python3
# Hamud001


def no_c(my_string):
    """function that removes all characters c and C ."""
    copy = [n for n in my_string if n != 'c' and n != 'C']
    return ("".join(copy))
