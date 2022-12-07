def maxProfit(arr):
    slow=0
    fast=1
    profit=0
    while fast<len(arr):
        if arr[slow]<arr[fast]:
            currentProfit=arr[fast]-arr[slow]
            profit=max(profit,currentProfit)
        else:
            slow=fast
        fast+=1
    return profit

a=maxProfit([1,2,4,2,5,7,2,4,9,0,9])
print(a)