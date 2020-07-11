# Write a python program to get a string from a given string where all occurences of its first char have been changed to '$',
# except the first char itself.

word = 'restart'

replacedWord = word[0] + word[1:].replace(word[0], "$")

print(replacedWord)
