#!/usr/bin/python3
import random
number = random.randint(-10, 10)

for w in number:
    if w > 0:
     print(w, "is positive")
    elif w == 0:
       print(w, "is zero")
    elif w < 0:
       print(w, "is negative")
