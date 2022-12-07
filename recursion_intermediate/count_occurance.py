def countOccurence(arr,n,x,i):
    if i==n:return 0
    small_ans=countOccurence(arr,n,x,i+1)
    if arr[i]==x:
        return small_ans+1
    else:
        return small_ans
    
a=countOccurence([5,5,6,5,6],5,5,0)
print(a)