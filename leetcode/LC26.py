arr=[0,0,1,1,1,2,2,3,3,4]
a=0
b=1
if not arr:
    print(0)
else:
    while b<len(arr):
        if arr[a]==arr[b]:
            b+=1
        else:
            a+=1
            arr[a],arr[b]=arr[b],arr[a]
            b+=1
    print(a+1)
    
    
        
