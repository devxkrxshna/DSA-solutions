def lastIndex(arr,n,x):
    if n==0:return -1
    if arr[n-1]==x:return n-1
    return lastIndex(arr,n-1,x)
a=lastIndex([1,2,3,4,5,5],6,5)
print(a)