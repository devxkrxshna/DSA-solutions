#array split at the beginning
def isArraySorted(arr,n): #function return a boolean value
    if n==0 or n==1:return True
    return arr[0]<arr[1] and isArraySorted(arr[1:],n-1)
a=isArraySorted([1,2,4,3],4)
print(a)
        