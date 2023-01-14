def twosum(nums,target):
    hasht={}
    for i,num in enumerate(nums):
        if target-num in hasht:
            return [hasht[target-num],i]
        else:
            hasht[num]=i
    return [-1,-1]
print(twosum([2,7,11,15],9))
        