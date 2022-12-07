def fizzBuzz(n):
    return['Fizz'*(i%3==0)+'Buzz'*(i%5==0) or str(i) for i in range(1,n+1)]

a=fizzBuzz(7)
print(a)