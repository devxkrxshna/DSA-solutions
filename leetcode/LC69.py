def addBinary(a,b):
    dec_a=0
    dec_b=0
    dec_a=sum(map(lambda x: int(x), [i for i in a]))
    dec_b=sum(map(lambda x: int(x), [i for i in b]))
    print(a+b)
    #a=bin(a+b).replace('0b','')
    return a+b

a= addBinary("101","101") 
print(a)  