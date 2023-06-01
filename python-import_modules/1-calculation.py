#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
for operator, operation in operators.items():
    result = operation(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
