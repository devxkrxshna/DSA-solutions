def geometric_sum(n):
    if n==0: return 1 #base case
    small_ans=geometric_sum(n-1) #small problem
    return small_ans+1/(2**(n)) #final_probkem=small_problem + last problem

a=geometric_sum(3)
print(a)