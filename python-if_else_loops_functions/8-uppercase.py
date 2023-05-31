#!/usr/bin/python3


def uppercase(str):
    for c in str:
        uppercase_char = chr(ord(c) - 32) if 97 <= ord(c) <= 122
        else c
        print("{}".format(uppercase_char), end="")
    print()
