# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

firstKey = 1
lastKey = 15

data = {}
for item in range(firstKey, lastKey + 1):
    data[item] = item*item


print(data)
