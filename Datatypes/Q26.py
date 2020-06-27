# Write a python program to insert a given string at the beginning of all items in a list

data = ['easy', 'important', 'wanted']
prefix = 'un'


def prefixWord(word): return prefix + word


result = map(prefixWord, data)
print(list(result))
