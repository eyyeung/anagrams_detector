# Anagrams detector
## Description
Python functions to detect whether two words are anagrams of each other 
## Functions
s1 and s2 are the two words as strings
* anagramsSort(s1,s2) : sort them alphabetically then check if they equal each other , uses O(n^2) time
* anagramsDict(s1, s2) : counting how many letters each word has and check whether the number of letters equal, uses O(n) time

## Examples
```python
print(anagramsDict('abcd','cdab')) # This should return True

print(anagramsDict('children','mother')) # This should return False

print(anagramsDict('child','baby')) # This should return False
```