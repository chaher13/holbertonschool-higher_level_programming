#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 10):
        separator = ", " if i < 8 or j < 9 else "\n"
        print("{:d}{:d}".format(i, j), end=separator)
