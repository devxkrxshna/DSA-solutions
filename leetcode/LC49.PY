from collections import defaultdict


def groupAnagrams(str):
    res=defaultdict(list) #setting default factory as list
    for s in str:
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")]+=1 #converting the occurence of a-z into an array
        res[tuple(count)].append(s)  #appending 
    return res   

a= groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)