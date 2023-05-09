#!/usr/bin/python3
import sys

def exit_with(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)

exit_with("and that piece of art is useful - Dora Korpar, 2015-10-19")
