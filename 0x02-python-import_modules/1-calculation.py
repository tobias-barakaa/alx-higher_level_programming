#!/usr/bin/python3
# 1-calculation.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div

        a, b = 10, 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
