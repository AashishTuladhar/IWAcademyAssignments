# Write a Python program to find if a given string starts with a given character using Lambda.

word = "Python"

result = lambda x: True if x[0] =='P' else False
print(result(word))