# Write a Python program to remove an item from a tuple.

data = ('a', 'b', 'c', 'd', 'e')

listData = list(data)
removedData = listData.pop(1)
result = tuple(listData)
print(result)
