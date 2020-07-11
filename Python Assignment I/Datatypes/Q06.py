# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

firstSample = 'The lyrics is not that poor!'
secondSample = 'The lyrics is poor!'


def checkConditionAndReplace(word, replacingWord):
    not_index = word.find('not')
    poor_index = word.find('poor')

    if not_index > 0 and poor_index > not_index:
        word = word.replace(word[not_index: poor_index + 4], replacingWord)

    return word


print(checkConditionAndReplace(firstSample, 'good'))
print(checkConditionAndReplace(secondSample, 'good'))
