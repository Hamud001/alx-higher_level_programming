#!/usr/bin/python3
# 2-args.py
# Hamud001

if __name__ == "__main__":
    """a program that prints the num of and the list."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
