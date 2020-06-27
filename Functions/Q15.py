# Write a Python program to filter a list of integers using Lambda.

data = [1, 4, 6, 10, 4, 12]

result = list(filter(lambda x:x>5, data))
print(result)
