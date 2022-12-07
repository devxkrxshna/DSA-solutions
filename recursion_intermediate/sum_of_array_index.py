#using index position method
def sumOfArray(arr,n,i):
    if n==i:return 0
    small_ans=sumOfArray(arr,n,i+1)
    return small_ans+arr[i]
a=sumOfArray([1,2,3,4],4,0)
print(a) 