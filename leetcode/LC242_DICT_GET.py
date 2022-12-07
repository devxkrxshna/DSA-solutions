def isAnagram(s,t):
    dict_s,dict_t={},{}
    for c in s:
        dict_s[c]=dict_s.get(c,0)+1
    for c in t:
        dict_t[c]=dict_t.get(c,0)+1
    return dict_s==dict_t

a=isAnagram(s = "anagram", t = "nagaram")
print(a)
    