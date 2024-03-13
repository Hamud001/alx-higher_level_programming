#!/usr/bin/python3
for num in range(0, 9):
    for k in range(num + 1, 10):
        if num == 8 and k == 9:
            print("{:d}{:d}".format(num, k))
        else:
            print("{:d}{:d}".format(num, k), end=", ")
