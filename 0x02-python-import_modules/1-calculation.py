#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a, b = 10, 5
    results = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    ops = ["+", "-", "*", "/"]
    for op, res in zip(ops, results):
        print("{} {} {} = {}".format(a, op, b, res))
