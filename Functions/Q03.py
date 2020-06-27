# Write a Python function to multiply all the numbers in a list.

data = [8, 2, 3, -1, 7]


def multiplyListItems(listData):
    product = 1
    for item in listData:
        product = product * item
    return product


print(multiplyListItems(data))
