# Write a Python program to count the occurrences of each word in a given sentence.

sentence = 'This is a sentence which is supposed to repeat one of its words.'
splitSentenceIntoWords = sentence.split()
occurences = {}

for word in splitSentenceIntoWords:
    if word in occurences:
        occurences[word] += 1
    else:
        occurences[word] = 1

print(str(occurences))
