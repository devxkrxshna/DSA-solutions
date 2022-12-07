def count(n):
    if n<1:return 0 #base case
    small_ans=count(n/10) #solving the smaller problem which is 4025
    return small_ans+1 #returning the small_ans+1


a=count(1089)
print(a)
    