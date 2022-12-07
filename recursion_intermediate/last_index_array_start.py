#iterating from the start
def lastIndex(arr,n,x,i):
    if i==n: return -1
    smallans=lastIndex(arr,n,x,i+1)
    if smallans==-1:
        if arr[i]==x:return i
        else:
            return -1
    else:
        return smallans
a=lastIndex([1,2,3,4,5,5,7],n=7,x=4,i=0)
print(a)


