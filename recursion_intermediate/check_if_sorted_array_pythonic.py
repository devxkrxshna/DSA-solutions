#array split at the end
def ifSorted(arr,n):
    if n==0 or n==1: return True
    if arr[-1]<arr[-2]:return False
    small_ans=ifSorted(arr,n-1)
    return small_ans

a=ifSorted([1,2,3,4],4)
print(a)
    