def fib(n):
    if n>0:
        if n==1 or n==2:
            fib=1
        elem1=1
        elem2=1
        for i in range(1,n-1):
            
            fib=elem1 + elem2
            elem2=elem1
            elem1=fib
            
        return fib
    return None

for i in range(1,10):
    print(i, "->",fib(i))