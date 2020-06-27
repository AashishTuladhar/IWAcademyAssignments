# Write a Python function to sum all the numbers in a list.

from functools import reduce

data = [1, 2, 3, 4]


def add(a, b): return a + b


def addItemsInList(listData):
    return reduce(add, listData)


print(addItemsInList(data))
