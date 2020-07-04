# Write a function, is_prime, that takes an integer and returns True if the number is prime and False if the number is not prime.

def is_prime(numberToCheck):
    if numberToCheck > 1:
        for number in range(2,numberToCheck):
            if (numberToCheck % number) == 0:
                return False
        else:
            return True
    else:
        return False


print(is_prime(13))