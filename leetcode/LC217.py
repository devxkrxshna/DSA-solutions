def containsDuplicate(arr):
    dictt={}
    for i in arr:
        if i not in dictt:
            dictt[i]=1
        else:
            return True
    return False
    

a=containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(a)