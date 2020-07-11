# Write a Python function to find the Max of three numbers.

from functools import reduce


def largestOfTwoNumbers(a, b): return a if a > b else b


def largestNumber(a, b, c):
    return reduce(largestOfTwoNumbers, [a, b, c])


print(max(11, 34, 4))
