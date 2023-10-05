#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    from sys import argv, exit
arg = len(argv)
if arg - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
sign = {"+": add, "-": sub, "*": mul, "/": div}
if argv[2] not in list(sign.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
a = int(argv[1])
b = int(argv[3])
print("{} {} {} = {}".format(a, argv[2], b, sign[argv[2]](a, b)))
