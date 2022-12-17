def containsNearbyDuplicates(nums,k):
    item={}
    for i,num in enumerate(nums):
        if num in item and abs(item[num]-i)<=k:
            return True
        item[num]=i
    return False
print(containsNearbyDuplicates([1,2,3,1],3))