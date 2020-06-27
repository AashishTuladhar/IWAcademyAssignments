# Write a Python function to insert a string in the middle of a string.


def insertStringInMiddle(containerWord, wordToInsert):
    middleIndex = int(len(containerWord)/2)
    return containerWord[0:middleIndex] + wordToInsert + containerWord[middleIndex:]


print(insertStringInMiddle('LearnToday', ' Python '))
