# Write a python program to check whether all dictionaries in a list or empty or not.

data = [{}, {}]

print('Empty dictionaries in list') if all(
    len(item) == 0 for item in data) else print('Not empty')
