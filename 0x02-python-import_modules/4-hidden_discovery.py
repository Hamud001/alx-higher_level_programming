#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    num = dir()
    for i in range(0, len(num)):
        if num[i][:2] !="__":
           print("{:s}".format(num[i]))
