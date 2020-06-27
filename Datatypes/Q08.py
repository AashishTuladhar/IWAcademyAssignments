# Write a Python program to remove the nth index character from a nonempty string.

nonEmptyWord = "Python"
index = 1

characterAtIndexRemoved = nonEmptyWord[0: index:] + \
    nonEmptyWord[index + 1::] if index < len(nonEmptyWord) else nonEmptyWord

print(characterAtIndexRemoved)
