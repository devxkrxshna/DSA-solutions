def fact(n):
    if n<0:return -1
    if n==0:return 1
    small_ans=fact(n-1)
    return small_ans*n



a=fact(-1)
print(a)