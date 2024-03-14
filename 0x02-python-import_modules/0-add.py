#!/usr/bin/python3
def add(a, b):
    from add_0 import add
    b = 2
    a = 1
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
