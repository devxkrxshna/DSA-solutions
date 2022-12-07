def twoSum(arr,targetsum):
    for i in range(len(arr)):
        firstNum=arr[i]
        for j in range(i+1,len(arr)-1):
            secondNum=arr[j]
            if targetsum==firstNum+secondNum:
                return [firstNum,secondNum]
    return []

a=twoSum([2,7,11,15],9)
print(a)