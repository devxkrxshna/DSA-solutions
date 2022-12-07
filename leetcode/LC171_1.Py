def titleToNumber(str):
    pos,sum=0,0
    for ch in reversed(str):
        digit=ord(ch)-64
        sum+=digit*26**pos
        pos+=1
        
    return sum
    
a=titleToNumber("A")
print(a)
        