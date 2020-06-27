# Write a Python program to check whether a given string is number or not using Lambda.

number = '2'

result = lambda x:True if x[0].isdigit() else False
print(result(number))