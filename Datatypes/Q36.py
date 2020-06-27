# Write a Python program to sum all the items in a dictionary.

from functools import reduce

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}


def addDictionaryValues(a, b): return a + b


totalSumOfValues = reduce(addDictionaryValues, data.values())
print(totalSumOfValues)
