#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10

# Last digit of 4205 is 5 and is less than 6 and not 0
if number > 5:
    print("Last digit of", number, "is", last, "and is greater than 5")
elif number == 0:
    print("Last digit of", number, "is", last, "and is 0")
elif (number < 6) and (last != 0):
    print("Last digit of", number, "is", -last, "and is less than 6 and not 0")
