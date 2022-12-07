def mult(m,n): #let m be the bigger and n be the smaller value
    if n==1:return m #base case
    small_ans=mult(m,n-1) #smaller problem
    return small_ans+m #bigger problem
    
a=mult(4,3)
print(a)