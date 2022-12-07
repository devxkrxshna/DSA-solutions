def removeDuplicates(s):
    stack=[]
    for i in s:
        if len(stack)==0 or i!=stack[-1]:
            stack.append(i)
        elif i==stack[-1]:
            stack.pop()
    return "".join(stack[::-1])
        
        
a=removeDuplicates("baacb")
print(a)