# to see if two words are anagrams of each other by first sorting then compare
# This uses sorting which takes O(n^2) time
def anagramsSort(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        list1=list(s1)
        list2=list(s2)

        list1.sort()
        list2.sort()

        pos = 0
        matches = True

        while pos < len(s1) and matches:
            if list1[pos] == list2[pos]:
                pos +=1
            else:
                matches = False
        return matches

#print(anagrams('abcd','cdab')) # This should return True

# Instead of sorting, use a dictionary , this is O(n) time but uses more space
def anagramsDict(s1, s2):
    if len(s1)!=len(s2):
        return False
    else:
        dict1={}
        dict2={}

        for word in s1:
            if word not in dict1:
                dict1[word] = 1
            else:
                dict1[word] += 1
        for word in s2:
            if word not in dict2:
                dict2[word] = 1
            else:
                dict2[word] += 1
        matches = True
        for key in dict1.keys():
            if dict1[key] == dict2[key]:
                matches = True
            else:
                return False
        return matches

print("The two words are: abcd, cdab. They are anagrams, should return true: ",anagramsDict('abcd','cdab'),) # This should return True
print("The two words are: children, mother. They are not anagrams, should return False: ",anagramsDict('children','mother'),) # This should return False
print("The two words are: child, baby. They are not anagrams, should return False: ",anagramsDict('child','baby'),) # This should return False

