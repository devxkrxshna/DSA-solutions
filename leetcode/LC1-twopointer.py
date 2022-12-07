def twoSum(arr,targetsum):
    arr.sort()
    head=0
    tail=len(arr)-1
    while(head<tail):
        currentsum=arr[head]+arr[tail]
        if currentsum==targetsum:
            return [arr[head],arr[tail]]
        elif currentsum>targetsum:
            tail-=1
        elif currentsum<targetsum:
            head+=1
    return []



a=twoSum([2,7,11,15],9)
print(a)