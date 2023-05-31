#!/usr/bin/python3
from add_0 import add as add_function
a = 1
b = 2
if __name__ == "__main__":
    result = add_function(a, b)
    print("{} + {} = {}".format(a, b, result), end="\n")
