#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
arg = len(argv)
if arg == 1:
    print(0)
else:
    add = 0
    for i in range(arg - 1):
        add += int(argv[i + 1])
    print("{}".format(add))
