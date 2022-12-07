def createTargetArray(nums,index):
    target=[]
    for i in range(len(nums)):
        target.insert(index[i],nums[i])
    return target
a=createTargetArray([0,1,2,3,4],[0,1,2,2,1])
print(a)
        