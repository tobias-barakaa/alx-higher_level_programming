#!/usr/bin/python3
"""Module to handle basic operations."""

from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, operator, b = args
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    try:
        a, b = int(a), int(b)
    except ValueError:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
