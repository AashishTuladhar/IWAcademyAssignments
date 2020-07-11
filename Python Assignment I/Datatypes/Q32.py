# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

numberRange = int(input('Enter end-range (Starts from 1):'))
result = {}

for item in range(1, numberRange+1):
    result[item] = item*item

print(result)
