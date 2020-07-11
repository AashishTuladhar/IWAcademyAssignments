# write a python program to replace the last element in a list with another list.

mainList = [1, 3, 5, 7, 9, 10]
newList = [2, 4, 6, 8]

mainList[-1:] = newList

print(mainList)
