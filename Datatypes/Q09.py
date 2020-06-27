# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

word = 'Python'


def exchangeInitial(word):
    if len(word) <= 1:
        return word

    return word[len(word) - 1] + word[1: len(word) - 1] + word[0]


print(exchangeInitial(word))
