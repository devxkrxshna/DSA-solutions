def checkInclusion(s1,s2):
    from collections import Counter
    d1=Counter(s1)
    k=len(s1)
    for i in range(len(s2)):
        sub=s2[i:i+k]
        d2=Counter(sub)
        if d1==d2: return True
    return False
a=checkInclusion(s1 = "ab", s2 = "eidbaooo")
print(a)
               
        