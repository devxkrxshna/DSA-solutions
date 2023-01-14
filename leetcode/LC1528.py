def restoreString(s,indices):
    j=0
    str=[]
    hash={}
    for i in indices:
        hash[i]=s[j] # add i as key and s[j] as value in the hashtable
        j+=1
    for i in range(len(indices)):#0-2
        str.append(hash[i])
    return "".join(str)
print(restoreString("abc",[1,0,2]))
        





