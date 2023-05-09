#!/usr/bin/python3

for let in range(97, 123):
    if chr(let) not in ['e', 'q']:
        print("{}".format(chr(let)), end="")
