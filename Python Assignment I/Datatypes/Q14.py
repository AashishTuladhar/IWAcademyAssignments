# Write a Python function to create the HTML string with tags around the word(s).


def htmlString(tag, word):
    return f"<{tag}>{word}</{tag}>"


print(htmlString('b', 'Python'))
