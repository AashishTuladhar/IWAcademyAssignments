# Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com

word = 'google.com'
characterFrequency = {}

for letter in word:
    if letter in characterFrequency:
        characterFrequency[letter] += 1
    else:
        characterFrequency[letter] = 1

print("Character frequency of '%s' is " % word + str(characterFrequency))
