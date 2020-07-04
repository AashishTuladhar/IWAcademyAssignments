# Create a list with the names of friends and colleagues. Search for the name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

nameList = ["Mary", "Adam", "Clint", "Jenny", "John"]

for name in range(len(nameList)):
    if "john" in nameList[name].lower():
        print("Name exists in the list")
        break
    elif "john" not in nameList[name].lower() and name == len(nameList) - 1:
        print("Not found")
