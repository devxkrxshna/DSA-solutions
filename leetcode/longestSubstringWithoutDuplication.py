


def longestSubstring(str):
    startidx=0
    hash={}
    endidx=0
    for i in range(len(str)):
        if str[i] not in hash:
            hash[str[i]]=i
        elif str[i] in hash:
            endidx=max(endidx,i)
            startidx=max(startidx,hash[str[i]]+1)
            print(startidx)
            hash[str[i]]=i
    ans=str[startidx:endidx]
    return ans
            
a=longestSubstring("clementisacap")
print(a)
    