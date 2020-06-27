# Write a python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

firstWord = 'abc'
secondWord = 'xyz'

swappedFirstWordInitial = firstWord.replace(firstWord[0:2], secondWord[0:2])
swappedSecondWordInitial = secondWord.replace(secondWord[0:2], firstWord[0:2])

combinedResult = swappedFirstWordInitial + ' ' + swappedSecondWordInitial
print(combinedResult)
