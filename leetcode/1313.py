def decompressRLElist(nums):
    ree=[]
    for i in [n for n in range(len(nums)) if n%2==0]:
        res=nums[i:2+i]
        for i in range(res[0]):
            ree.append(res[1])
    return ree
            
        
print(decompressRLElist([1,1,2,3]))
        