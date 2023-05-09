#!/usr/bin/python3
import random

number = random.randint(-10, 10)

for w in str(abs(number)):
    digit = int(w)
    if digit > 0:
        print(digit, "is positive")
    elif digit < 0:
        print(digit, "is negative")
    else:
        print(digit, "is zero")
