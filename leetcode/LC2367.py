def arithmeticTriplets(nums,diff):
    count=0
    for num in nums:
        if num+diff in nums and num+2*diff in nums:
            count+=1
    return count
print(arithmeticTriplets([0,1,4,6,7,10],3))   


    

def arithmeticTriplets(nums,diff):
    hasht={}
    count=0
    for i,num in enumerate(nums):
        if num-diff in hasht and num-2*diff in hasht:
            #print(num,num-diff,num-2*diff)
            count+=1
        hasht[num]=i
    return count

print(arithmeticTriplets([0,1,4,6,7,10],3)) 