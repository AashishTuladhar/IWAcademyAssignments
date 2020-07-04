# Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

num1 = float(input("Enter a number:"))
num2 = float(input("Enter another number:"))
operatorSelected = input("Enter operator (+ = Sum, - = Difference, * = Multiplication, / = Division):")

if operatorSelected == '+':
    print(num1 + num2)
elif operatorSelected == '-':
    print(num1 - num2)
elif operatorSelected == "*":
    print(num1 * num2)
elif operatorSelected == '/':
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Division by zero is not possible. Please try any other number.")
else:
    print("Invalid Operator")