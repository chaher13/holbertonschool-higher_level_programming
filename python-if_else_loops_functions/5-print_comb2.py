#!/usr/bin/python3

for i in range(100):
    separator = ", " if i < 99 else "\n"
    print('{:02d}'.format(i), end=separator)
