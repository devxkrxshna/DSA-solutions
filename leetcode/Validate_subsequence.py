def validateSubsequence(arr,tar):
    tar_i=0
    for i in arr:
        if tar_i==len(tar):
            return True
        if i==tar[tar_i]:
            tar_i+=1
    return tar_i==len(tar)

a=validateSubsequence([5,1,122,25,6,-1,8,10],[1,6,-1,10])
print(a)
                
                