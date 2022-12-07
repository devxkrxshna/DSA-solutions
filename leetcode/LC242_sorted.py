def isAnagram(s,t):
    return sorted(s)==sorted(t)

a=isAnagram(s = "anagram", t = "nagaram")
print(a)
    