# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

inputNumber = int(input("Enter a number:"))

def multiply(number):
    multiple = number * inputNumber
    return multiple

print(multiply(10))