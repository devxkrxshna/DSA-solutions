def checkIfPangram(str):
    hasht={}
    new_str=[]
    j=97
    for i in range(26):
        if chr(j) not in hasht:
            hasht[chr(j)]=1
        j+=1
    for s in str:
        if s not in new_str:
            new_str.append(s)
    for s in new_str:
        if s in hasht:
            hasht[s]-=1
    for c in hasht:
        if hasht[c]!=0:
            return False
    return True
    
def checkIfPangram(s):
    return len(set(s)) == 26
print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
