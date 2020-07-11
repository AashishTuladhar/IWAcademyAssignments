# Write a Python function that takes a list and returns a new list with unique elements of the first list.

data = [1, 2, 3, 3, 4, 5, 5]


def uniqueList(listData):
    return set(listData)


uniqueData = list(uniqueList(data))
print(uniqueData)
