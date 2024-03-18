#!/usr/bin/python3
# 1-element_at.py
# Hamud001


def element_at(my_list, idx):
    """function that retrieves an element."""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
