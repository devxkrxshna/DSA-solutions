def shuffleArray(nums,n):
    newNums=[]
    j=n
    for i in range(0,n):
            newNums.append(nums[i])
            newNums.append(nums[j])
            j+=1      
    return newNums

a=shuffleArray([1,2,3,4,5,6],3)
print(a)
            
            
    