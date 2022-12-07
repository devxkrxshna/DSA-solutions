def fib(n):
    if n==0:return 0 #base case 1
    if n==1:return 1 #base case 2
    ans_1=fib(n-1)+fib(n-2) # induction hypothesis
    return ans_1 

a=fib(6)
print(a)