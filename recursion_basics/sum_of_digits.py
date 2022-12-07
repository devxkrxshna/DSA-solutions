def sumofdigits(n):
    if n<1:return 0
    small_ans=sumofdigits(n//10)
    return small_ans+n%10
    
a=sumofdigits(1237)
print(a)