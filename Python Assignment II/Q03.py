# Write code that will print out the anagrams (words that use the same letters) from a paragraph of text.

from collections import defaultdict  
  
def getAnagrams(wordsList): 
    groupedWords = defaultdict(list) 
  
    for word in wordsList: 
        groupedWords["".join(sorted(word))].append(word) 
  
    for group in groupedWords.values(): 
        print(" ".join(group))       
  
  
 
wordsList =  ["mane", "name", "mean", "live", "evil", "tab", "bat"]   
getAnagrams(wordsList)