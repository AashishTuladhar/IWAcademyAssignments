# Write a Python program to sort a list of dictionaries using Lambda.

data = [{'f': 6, 'b': 6, 'e': 5},{'d':4,'b': 3,'a':1},{'h': 8,'b':1,'i':9}]
result = sorted(data, key=lambda sortDictionary: sortDictionary['b'])

print(result)