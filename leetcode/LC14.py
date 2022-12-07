def longestCommonPrefix(s):
    min_string= min(s,key=len)
    for i,ch in enumerate(min_string):
        for other in s:
            if other[i]!=ch:
                return min_string[:i]        
                
    return min_string


a=longestCommonPrefix(["flower","flow","flight"])
print(a)