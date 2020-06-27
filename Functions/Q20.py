# Write a Python program to find intersection of two given arrays using Lambda.

array1 = [1, 3, 5, 7, 9, 0]
array2 = [2, 4, 6, 8, 10, 0]

intersection = list(filter(lambda x: x in array1, array2))
print(intersection)