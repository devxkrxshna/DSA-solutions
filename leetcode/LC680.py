
def check(str,new_head,new_tail):
    while(new_head<new_tail):
        if str[new_head]!=str[new_tail]:
            return False
        new_head+=1
        new_tail-=1
    return True
    
            

def validPalindrome2(str):
    head=0
    tail=len(str)-1
    while head<tail:
        if str[head]!=str[tail]:
            return check(str,head+1,tail) or check(str,head,tail-1)        
        head+=1
        tail-=1
    return True
        
        
        
a=validPalindrome2("aba")
print(a)
    