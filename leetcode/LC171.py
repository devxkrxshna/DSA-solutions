def titleToNumber(str):
    str=str.upper()
    sum=0
    power=1
    for i in reversed(range(0,len(str))):
         digit=ord(str[i])-64
         sum=digit+power*sum
         power=power*26
    return sum

a=titleToNumber("A")
print(a)
        
        
        
        
        