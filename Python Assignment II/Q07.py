# Create a list of tuples of first name, last name, and age for your friends and colleagues. 
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. 
# Print out each name, followed by old or young if they are above or below the average age.

infoList = [("Aashish","Tuladhar",24),("Aman","Maharjan",None),("Ravi","Shrestha",26)]

listWithoutNoneValue = [index for index in infoList if index[2] != None]
ageList = [index[2] for index in listWithoutNoneValue if index[2]] 
averageAge = sum(ageList)/len(ageList)

for age in listWithoutNoneValue:
    if age[2] > averageAge:
        print(age, "Old")
    else:
        print(age, "Young")