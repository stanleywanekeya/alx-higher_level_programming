#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
i = len(argv)
if i == 1:
    print("{} arguments.".format(i - 1))
elif i == 2:
    print("{}: argument:\n{}: {}".format(i - 1, i - 1, argv[i - 1]))
else:
    print("{}: arguments".format(i - 1))
    for j in range(i - 1):
        print("{}: {}".format(j + 1, argv[j + 1]))
