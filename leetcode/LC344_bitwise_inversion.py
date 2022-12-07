def reverseString(s):
    for i in range(len(s)//2):
        s[i],s[~i]=s[~i],s[i]
    return s

a=reverseString(["h","e","l","l","o"])
print(a)