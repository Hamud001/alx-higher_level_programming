#!/usr/bin/python3
def print_arg(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d} argument.".format(num))
        return
    else:
        if num == 1:
            print("{:d} argument:".format(num))
        else:
            print("{:d} arguments:".format(num))
        n = 1
        while n <= num:
            print("{:d}: {:s}".format(n, argv[n]))
            n += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
