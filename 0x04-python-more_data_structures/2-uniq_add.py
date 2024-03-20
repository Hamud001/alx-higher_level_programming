#!/usr/bin/python3
# Hamud001


def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list."""
    unique_nums = set(my_list)
    return sum(unique_nums)
