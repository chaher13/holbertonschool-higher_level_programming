#!/usr/bin/python3
a = 1
b = 2

from add_0 import add as add_function

if __name__ == "__main__":
    result = add_function(a, b)
    print("{} + {} = {}".format(a, b, result))
