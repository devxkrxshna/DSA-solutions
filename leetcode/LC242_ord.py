def isAnagram(s,t):
    mem1,mem2=[0]*26,[0]*26
    for c in s:
        mem1[ord(c)-ord("a")]+=1
    for c in t:
        mem2[ord(c)-ord("a")]+=1
    return mem1==mem2

a=isAnagram(s = "anagram", t = "nagaram")
print(a)
    