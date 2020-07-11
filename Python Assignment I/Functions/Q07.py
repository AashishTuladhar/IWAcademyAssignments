# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def countOfUppercaseAndLowercase(data):
    uppercaseCount = 0
    lowercaseCount = 0

    for i in data:
        if (i.isupper()):
            uppercaseCount += 1
        elif (i.islower()):
            lowercaseCount += 1
        else:
            pass

    return f'Uppercased Letters: {uppercaseCount}, Lowercased letters: {lowercaseCount}'


print(countOfUppercaseAndLowercase('ThiS is A WeiRd SenTeNCe'))
