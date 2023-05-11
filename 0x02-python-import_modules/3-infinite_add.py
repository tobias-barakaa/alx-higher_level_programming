#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys

    all = 0
    for n in range(len(sys.argv) - 1):
        all += int(sys.argv[n + 1])
    print("{}".format(all))
