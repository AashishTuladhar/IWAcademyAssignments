# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


def factorialValue(number):
    if number == 0 or number == 1:
        return 1
    elif number < 0:
        return 0
    else:
        return number * factorialValue(number-1)


print(factorialValue(10))
