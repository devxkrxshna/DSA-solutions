def Storepos(arr,n,x,i=0,arr2=[]):
    if i==n:return 
    if arr[i]==x:arr2.append(i)
    print(i)
    small_ans=Storepos(arr,n,x,i+1)
    return small_ans
arr2=[]
a=Storepos([5,5,6,5,6],5,5,0,arr2)
print(a)