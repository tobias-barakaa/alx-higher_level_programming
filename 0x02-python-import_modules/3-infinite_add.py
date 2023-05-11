#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:] # get all command line arguments except the first one (which is the name of the script itself)
    sum = 0
    for arg in args:
        sum += int(arg)
    print(sum)
