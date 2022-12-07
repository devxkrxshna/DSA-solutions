def validParanthesis(strs):
    stack=[]
    head=0
    while(head<len(strs)):
        if strs[head]=="[":
            stack.append(strs[head])
            head+=1
        if strs[head]=="]":
            if stack[-1]=='[':
                stack.pop()
            head+=1
        if strs[head]=="(":
            stack.append(strs[head])
            head+=1
        if strs[head]==")":
            if stack[-1]=='(':
                stack.pop()
            head+=1
        if strs[head]=="{":
            stack.append(strs[head])
            head+=1
        if strs[head]=="}":
            if stack[-1]=='{':
                stack.pop()
            head+=1
            
a=validParanthesis("[]()")
print(a)
        
        
        
            