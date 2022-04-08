def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for i in range(100):
    if i in potenciasDe2(6):
        print(i)

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(Fib(10))

print(fibs)