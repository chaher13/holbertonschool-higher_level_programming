#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 0:
        print(0)
        resultat = 0
    for i in range(1, len(argv)):
        x = int(argv[i])
        resultat = resultat + x
        print(resultat)
