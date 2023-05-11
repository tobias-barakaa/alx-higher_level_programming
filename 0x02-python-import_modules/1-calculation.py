#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a, b = 10, 5
    results = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    ops = ["+", "-", "*", "/"]
    for i in range(len(results)):
        print("{} {} {} = {}".format(a, ops[i], b, results[i]))
    for op, func in zip(ops, [add, sub, mul, div]):
        print("{} {} {} = {}".format(a, op, b, func(a, b)))
