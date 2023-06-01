#!/usr/bin/python3
from sys import argv
args = argv[1:]
num_args = len(args)
print("{} argument{}".format(num_args, 's' if num_args != 1 else ''), end='')
print('.' if num_args == 0 else ':')
for i, arg in enumerate(args, start=1):
    print("{} {}".format(i, arg))
