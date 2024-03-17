#!/usr/bin/python3
import hidden_4


def discovr():
    name = dir(hidden_4)
    for n in name:
        if n[:2] != '__':
            print("{:s}".format(n))


if __name__ == "__main__":
    discovr()
