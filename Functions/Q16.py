# Write a Python program to square and cube every number in a given list of integers using Lambda.

data = [1, 4, 6, 10, 4, 12]

square = list(map(lambda x: x ** 2, data))
cube = list(map(lambda x: x ** 3, data))

print(square)
print(cube)