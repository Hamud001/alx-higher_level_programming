#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv)  != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = argv[2]
    sum1 = int(argv[1])
    sum2 = int(argv[3])

    if ops is '+':
        print("{:d} + {:d} = {:d}".format(sum1, sum2, add(sum1, sum2)))
    elif ops is '-':
        print("{:d} - {:d} = {:d}".format(sum1, sum2, sub(sum1, sum2)))
    elif ops is '*':
        print("{:d} * {:d} = {:d}".format(sum1, sum2, mul(sum1, sum2)))
    elif ops is '/':
        print("{:d} / {:d} = {:d}".format(sum1, sum2, div(sum1, sum2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
