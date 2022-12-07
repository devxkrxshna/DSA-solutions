#array split at the end
def ifSorted(arr,n):
    if n==0 or n==1:return True
    if arr[-1]<arr[-2]:
        return False
    if ifSorted(arr,n-1):
        return True
    else:
        return False
    
a=ifSorted([32,54,89,90,8],5)
print(a)
    