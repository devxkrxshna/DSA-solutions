def validParanthesis(str):
    clean_str="".join([ch.lower() for ch in str if ch.isalnum()])
    head=0
    tail=len(clean_str)-1
    while(head<tail):
        if clean_str[head]!=clean_str[tail]:
            return False
        head+=1
        tail-=1
    return True

a=validParanthesis("A man, a plan acanal: panama")
print(a)