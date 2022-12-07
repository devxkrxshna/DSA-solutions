def sumofDigits(n):
    if n<1: return 0
    lastdigit=n%10
    small_ans=sumofDigits(n//10)
    return small_ans+lastdigit


a=sumofDigits(1237)
print(a)


#the value of n changes only in the next call stack