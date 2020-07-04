# Create a tuple with your first name, last name, and age. Create a list of people, and append your tuple to it. 
# Make more tuples with the corresponding information from your friends and append them to the list. 
# Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

name = ("Aashish","Tuladhar",24)
name1 = ("Aman","Maharjan",26)
name2 = ("Ravi","Shrestha",25)

peopleList = list((name,)+(name1,)+(name2,))

print("Sorted by age:",sorted(peopleList, key=lambda sortTuple: sortTuple[2]))