def validParanthesis(str):
    head=0
    tail=len(str)-1
    while(head<tail):
        while not str[head].isalnum() and head<tail:head+=1
        while not str[tail].isalnum() and head<tail:tail-=1
        if str[head].lower()==str[tail].lower():
            head+=1
            tail-=1
        else:
            return False
    return True

a=validParanthesis("A man, a plan acanal: panama")
print(a)
        
        