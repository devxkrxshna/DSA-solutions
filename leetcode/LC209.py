def minSubArrayLen(target, arr):
    slow=0
    subArrSum=0
    res=float('inf')
    for fast in range(len(arr)):
        subArrSum+=arr[fast]
        while subArrSum>=target:
            res=min(res,fast-slow+1)
            subArrSum-=arr[slow]
            slow+=1
    return 0 if res==float('inf') else res

a=minSubArrayLen(7,[2,3,1,2,4,3])
print(a)
            
            
        
        
    









a=minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12])
print(a)
            
        
        
        