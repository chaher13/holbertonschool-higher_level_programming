#!/usr/bin/python3

for i in range(100):
    separator = ", " if i < 99 else "\n"
    print(f"{i:02d}", end=separator)
