def threeSum(arr,target):
    arr.sort()
    act_sum=[]
    for current in range(len(arr)):
        if current > 0 and arr[current] == arr[current- 1]: #remove duplicates
            continue
        l=current+1
        r=len(arr)-1
        while(l<r):
            current_sum=arr[current]+arr[l]+arr[r]
            if current_sum==target:
                act_sum.append([arr[current],arr[l],arr[r]])
                l+=1
                r-=1
            elif current_sum<target:
                l+=1
            elif current_sum>target:
                r-=1
    return act_sum
                
            
a=threeSum([-1,0,1,2,-1,-4],0)
print(a)