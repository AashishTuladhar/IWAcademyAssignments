# Write a Python function that takes a list of words and returns the length of the longest one.

words = ['python', 'function', 'that', 'takes', 'a', 'list', 'of', 'words',
         'and', 'returns', 'the', 'length', 'of', 'the', 'longest', 'one']

longestWord = max(words, key=len)
length = max(len(word) for word in words)

print(
    f'The longest word length in the list is: {length} (word: "{longestWord}").')
