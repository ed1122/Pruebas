def isPrime(num):
    #
# coloca tu código aquí
#
    x=1
    div=0
    while num >=x:
        if num % x==0:
            div+=1
        x+=1
    if div ==2:
        return True
    else:
        return False

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
        
print(isPrime(2000))