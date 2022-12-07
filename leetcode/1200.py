def minAbsDifference(arr):
    arr.sort()
    smallest=float('inf')
    for i in range(len(arr)-1):
        current=arr[i+1]-arr[i]
        if current<smallest:
            smallest=current
    
    dif=[]
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]==smallest:
            dif.append([arr[i+1],arr[i]])
    return dif
            
        
   
    
    
    
a=minAbsDifference([4,2,1,3])
print(a)
        