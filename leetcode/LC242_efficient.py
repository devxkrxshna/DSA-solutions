def isAnagram(s,t):
    dict={}
    for c in s:
        dict[c]=dict.get(c,0)+1
    for c in t:
        if c not in dict:
            return False
        else:
            dict[c]-=1
    for val in dict.values():
        if val!=0:
            return False
    return True

a=isAnagram(s = "anagram", t = "nagaram")
print(a)