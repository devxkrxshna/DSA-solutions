def arithmeticTriplets(nums,diff):
    count=0
    for num in nums:
        if num+diff and num+2*diff in nums:
            print(num,num+diff,num+2*diff)
            count+=1
    return count
print(arithmeticTriplets([0,1,4,6,7,10],3))        