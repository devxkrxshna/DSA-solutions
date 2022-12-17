def decode(encoded,first):
    res=[first]
    for i in range(len(encoded)):
        res.append(res[i]^encoded[i])
    return res

print(decode([1,2,3],1))
        
        
def decode2(encoded,first):
    res=[first]
    for a in encoded:
        res.append(res[-1]^a)
    return res

print(decode2([1,2,3],1))