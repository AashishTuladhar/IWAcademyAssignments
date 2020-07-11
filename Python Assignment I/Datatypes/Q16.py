# Write a Python program to sum all the items in a list.

from functools import reduce


def add(a, b): return int(a) + int(b)


data = ['1', '2', '3', '4', '5']

result = reduce(add, data)

print(result)
