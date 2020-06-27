# Write a Python function to check whether a number is in a given range.


def numberInRange(number):
    if number in range(0, 10):
        print("%s exists in the range" % str(number))
    else:
        print("%s doesn't exist in the range" % str(number))


numberInRange(3)
