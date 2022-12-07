def storePos(arr,n,x,i):
    mem=[]
    if n==i: return
    smallans=storePos(arr,n,x,i+1)
    if smallans is None:
        if arr[i]==x:
            mem.append(i)
    else:
        mem.append(i)
    return mem 
a=storePos([5,5,6,5,6],5,5,0)
print(a)