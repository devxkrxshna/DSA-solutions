

def lengthOfLongestSubstring(s):
    slow=0
    res=0
    charSet=set()
    for fast in range(len(s)):
        while s[fast] in charSet:
            charSet.remove(s[slow])
            slow+=1
            print(charSet)
        charSet.add(s[fast])
        res=max(res,fast-slow+1)
        
    return res

a=lengthOfLongestSubstring("pwwkew")
print(a)
        
        
        