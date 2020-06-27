# Write a Python program to sort a list of tuples using Lambda.

data = [(3,2),(1,3),(0,2),(3,5)]

result = sorted(data, key=lambda sortTuple: sortTuple[0])
print(result)