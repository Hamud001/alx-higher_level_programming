#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import
    num = dir()
    for i in range(0, len(num)):
        if num[i][:2] !="__":
           print("{:s}".format(num[i]))
