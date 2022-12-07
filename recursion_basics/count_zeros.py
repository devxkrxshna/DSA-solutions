def count_digits(n):
    if n==0: return 0
    small_ans=count_digits(n//10)
    if n%10==0:
        return small_ans+1
    else:
        return small_ans
    
a=count_digits(105006)
print(a)


#    10500|6
# count_zeros(10500) =3 | 6 , since 6 not equal to zero return 3+0=3
#        |
#    1050|0
# count_zeros(1050) =2 | 0, since its equal to zero return 2+1 =3
#        |
#      105|0
#
#count_zeros(105) =1 | 0, since its equal to zero return 1+1 =2
#        |
#     10|5
#count_zeros(10) =1 | 5 , since its equal to zero return 1+0 =1
#        |
#      1|0
#count_zeros(1) =0 | 0 , since its equal to zero return 0+1 =1
#      0|1 
#reached the base case, ie if n==0, return 0
#
#