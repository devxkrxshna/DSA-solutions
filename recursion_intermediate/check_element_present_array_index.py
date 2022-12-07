#very similar to the for loop approach

def isPresent(arr,n,x,i=0):
    if n==i:return False
    if arr[i]==x:return True
    elif isPresent(arr,n,i+1,x):
        return True
    else:
        return False
a=isPresent([1,2,4,3],4,1)
print(a)