def checkNum(arr,n,x):
    if n==0: return False #if the array is empty return False, ie element is not present in the array
    if arr[n-1]==x: #last case when we divide an array into the recursive part and the end part
        return True
    elif checkNum(arr,n-1,x): #smaller problem
        return True
    else:
        return False
a=checkNum([1,2,4,3],4,1)
print(a)

