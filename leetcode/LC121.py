def maxProfit(arr):
    maxP=0
    slow=0
    for fast in range(1,len(arr)):
        if arr[slow]<arr[fast]:
            currentProfit=arr[fast]-arr[slow]
            maxP=max(maxP,currentProfit)
        else:
            slow=fast
            
    return maxP

a=maxProfit([1,2,4,2,5,7,2,4,9,0,9])
print(a)