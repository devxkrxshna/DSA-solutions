


def isPresent(arr,n,x):
    if n==0:return False #base case
    if arr[0]==x: return True
    elif isPresent(arr[1:],n-1,x):
        return True
    else:
        return False
a=isPresent([1,2,4,3],4,1)
print(a)