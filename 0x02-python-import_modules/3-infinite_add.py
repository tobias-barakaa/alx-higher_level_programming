#!/usr/bin/python3
import sys

args = sys.argv[1:]
total = sum(int(arg) for arg in args)
print(total)
