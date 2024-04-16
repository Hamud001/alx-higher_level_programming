#!/usr/bin/python3
"""a function that appends a string at the end of UTF8."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8.
    Args:
        filename (str): The name of the file.
        text (str): The string to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
