# Write a python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

wordList = ['This', 'is', 'a', 'sentence']  # Sample

resultList = []

for word in wordList:
    count = len(word)

    if count < 2:
        result = ''
    else:
        result = word[0:2]+word[-2:]

    resultList.append(result)

print(resultList)
