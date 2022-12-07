def pow(x,n):
    if n==1: return x
    if n==0: return 1
    power=x*pow(x,n-1)
    return power

a=pow(7,2)
print(a)