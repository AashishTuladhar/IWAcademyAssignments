# Write a Python program to remove the characters which have odd index values of a given string.

word = "Python"

result = ''
for letter in range(len(word)):
    if letter % 2 == 0:
        result = result + word[letter]

print(result)
