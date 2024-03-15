#!/usr/bin/python3

if _name_ == "_main_":
    """Print all names defined by compiled module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "":
            print(name)
