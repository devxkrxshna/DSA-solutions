def maxprofit(arr):
    res=0
    a=0
    for b in range(1,len(arr)):
        if arr[a]<arr[b]:
            res=max(res,arr[b])
        else:
            a=b
    return res-arr[a]

print(maxprofit([7,1,5,3,6,4]))
    
        
        
        
            
    