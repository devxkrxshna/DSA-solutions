def productExceptSelf(nums):
    prefix=[]
    product=1
    postfix=[]
    res=[]
    for i in nums:
        product=product*i
        prefix.append(product)
    product=1
    for i in reversed(nums):
        product=product*i
        postfix.append(product)
    prefix.insert(0,1)
    postfix=postfix[::-1]
    postfix.append(1)
    for i in range(len(nums)):
        pro=prefix[i]*postfix[i+1]
        res.append(pro)
    return res
        
        

        
        
def  productExceptSelf(nums):
    res=[]
    product=1
    for i,num in enumerate(nums):
        if i-1==-1:
            res.append(1)
        else:
            product=product*nums[i-1]
            res.append(product)
    product=1
    for i in reversed(range(len(nums))):
        if i+1==len(nums):
            res[-1]=res[-1]*1
        else:
            product=product*nums[i+1]
            res[i]=product*res[i]
    return res
        
        
#not completed  (using Calculate product & divide by self method)      
# def productExceptSelf(nums):
#     product=1
#     count=0
#     for num in nums:
#         if num==0:
#             count+=1
#         else:
#             product=product*num
#     res=[product]*len(nums)
#     for i in range(len(nums)):
#         if count==1:
#             if num[i]!=0:
#                 res[i]=res[i]//nums[i]
#             else:
#                 res[i]=0
#         elif count>1:
#             res=[0]*len(nums)
#         else:
#             res[i]=res[i]//nums[i]
#     return res
        
    
        
              
    
print(productExceptSelf([1,2,3,4]))
        
        
        