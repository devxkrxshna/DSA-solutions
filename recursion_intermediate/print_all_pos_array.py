def printPos(arr,n,x,i):
    if i==n: return ""
    if arr[i]==x: print(i)
    small_ans=printPos(arr,n,x,i+1)
    return small_ans
a=printPos([5,5,6,5,6],5,5,0)
print(a)