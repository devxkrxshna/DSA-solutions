def smallerNumbersThanCurrent(nums):
    indices={}
    for idx,num in enumerate(sorted(nums)):
        indices.setdefault(num,idx)
    return [indices[num] for num in nums]
print(smallerNumbersThanCurrent([8,1,2,2,3]))