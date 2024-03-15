#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv)  != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = argv[2]
    int1 = int(argv[1])
    int2 = int(argv[3])

    if ops is '+':
        print("{:d} + {:d} = {:d}".format(int1, int2, add(int1, int2)))
    elif ops is '-':
        print("{:d} - {:d} = {:d}".format(int1, int2, sub(int1, int2)))
    elif ops is '*':
        print("{:d} * {:d} = {:d}".format(int1, int2, mul(int1, int2)))
    elif ops is '/':
        print("{:d} / {:d} = {:d}".format(int1, int2, div(int1, int2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
