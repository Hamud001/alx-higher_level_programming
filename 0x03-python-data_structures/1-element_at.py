#!/usr/bin/python3
# 1-element_at.py
# Hamud001


def element_at(my_list, idx):
    """function that retrieves an element."""
   if idx >= len(my_list) or idx < 0:
        return None
    return my_list[idx]
