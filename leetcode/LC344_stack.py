def reverseString(s): #input is an array of characters
    reverse=[]
    while(len(s)!=0):
        c=s.pop()
        reverse.append(c)
    return reverse

a=reverseString(["h","e","l","l","o"])
print(a)