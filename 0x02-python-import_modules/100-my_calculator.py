#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    i = len(argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    ops = argv[2]
    b = int(argv[3])
    if ops == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, add(a, b)))
    elif ops == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sub(a, b)))
    elif ops == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, mul(a, b)))
    elif ops == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    arg_calc(sys.argv)
