# Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.

def palindrome(wordToCheck):
    word = wordToCheck.lower().replace(" ","")
    if word == word[::-1]:
        print(f"'{wordToCheck}' is Palindrome")
    else:
        print(f"'{wordToCheck}' is not Palindrome")


palindrome("Noon")