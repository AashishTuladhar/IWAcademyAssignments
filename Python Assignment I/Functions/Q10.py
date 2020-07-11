# Write a Python program to print the even numbers from a given list.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []


def getEvemNumbers(listData):
    for item in listData:
        if item % 2 == 0:
            result.append(item)

    return result


print(getEvemNumbers(data))
