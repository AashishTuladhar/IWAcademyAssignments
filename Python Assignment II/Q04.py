# Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. 
# What is the first item on the list? What is the second item on the list?

nameList = []

print(id(nameList))

nameList.extend(["Bob", "Ryan", "Jenny", "Keith"])

print(id(nameList))

iterableList = iter(sorted(nameList))

print("First item of list:",iterableList.__next__())
print("Second item of list:",iterableList.__next__())
