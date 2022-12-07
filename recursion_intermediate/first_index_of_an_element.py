from re import I


def firstIndex(arr,n,x,i=0):
    if n==i:return -1
    if arr[i]==x:
        return i 
    smallans= firstIndex(arr,n,x,i+1)
    return smallans

a=firstIndex([1,2,3,4,4,5],6,4)
print(a)