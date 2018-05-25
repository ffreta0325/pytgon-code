def fib(n):
    a= 0
    b= 1
    #a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b

print(fib(3))
print(fib(5))
print(fib(7))

def fib2(n):
    a,b=0,1
    for i in range(1,n):
     c=a+b
     a=b
     b=c
    return b