#!/usr/bin/python3
#!cse(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()usr/bin/python3
