# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

text = input("Enter comma separated values: ")

splitText = text.split(',')
sortedUniqueWords = sorted(set(splitText))
result = ','.join(sortedUniqueWords)

print(result)
