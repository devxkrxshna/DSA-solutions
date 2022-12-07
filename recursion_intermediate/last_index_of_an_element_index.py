def lastIndex(arr,n,x,i):
    if i==-1:return -1
    if arr[i]==x:
        return i
    return lastIndex(arr,n,x,i-1)
a=lastIndex([1,2,3,4,5,5,7],n=7,x=4,i=6)
print(a)