#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a, b = 10, 5
    result = "{} {} {} {} {} {}".format(a, b, add(a, b), mul(a, b), sub(a, b), div(a, b))
    print(result)
