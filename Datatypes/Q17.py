# Write a Python program to multiply all the items in a list.

from functools import reduce

data = ['1', '2', '3', '4', '5']


def multiplication(a, b): return int(a) * int(b)


result = reduce(multiplication, data)
print(result)
