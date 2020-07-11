# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

word = 'test'
suffix = 'ing'

if len(word) > 3:
    if word.endswith(suffix):
        result = word + 'ly'
    else:
        result = word + suffix
else:
    result = word

print(result)
