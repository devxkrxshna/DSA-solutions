def summ(arr,n):
    if n==0:return 0 #base case
    small_ans=summ(arr,n-1) #smaller problem
    return small_ans+arr[n-1] #we use n-1 as index because thats the last list index( note: in python indexing starts from zero)

a=summ([1,2,3],3)
print(a)