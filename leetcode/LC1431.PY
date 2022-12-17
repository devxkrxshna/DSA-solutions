def kidsWithCandies(candies,extraCandies):
    res=[]
    maxCandie=max(candies)
    for i in candies:
         res.append((i+extraCandies)>=maxCandie)
    return res
print(kidsWithCandies([2,3,5,1,3],3))
            