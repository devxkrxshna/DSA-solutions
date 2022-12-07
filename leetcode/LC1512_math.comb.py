from math import comb
def NumberofGoodPairs(arr):
    dict={}
    count=0
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    print(dict)
    for key,value in dict.items():
        combination=comb(value,2)
        count+=combination
        
    return count

a=NumberofGoodPairs([1,1,1,1])
print(a)