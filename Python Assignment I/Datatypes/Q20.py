# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

data = ['abc', 'xyz', 'aba', '1211']


count = 0
for item in data:
    if item[0] == item[-1]:
        count += 1

print(count)
