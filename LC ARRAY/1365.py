def smallerNumbersThanCurrent(nums):
    count=0
    arr=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]>nums[j]:
                count+=1
        arr.append(count)
    
a=smallerNumbersThanCurrent([8,1,2,2,3])
print(a)