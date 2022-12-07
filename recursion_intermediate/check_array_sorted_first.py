#array split at the beginning
def isArraySorted(arr,n):
    if n==0 or n==1:return True #base case
    if arr[0]>arr[1]:
        return False
    small_ans=isArraySorted(arr[1:],n-1) #small problem
    return small_ans
a=isArraySorted([1,2,3,4],4)
print(a)
        
    