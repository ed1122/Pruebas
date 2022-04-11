'''lst = [1 if x % 2 == 0 else 0 for x in range(10)]
genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()
print(len(lst))

for v in genr:
    print(v, end=" ")
print()
print(len(genr))'''
'''
dos = lambda : 2
cuadrado = lambda x : x * x
potencia = lambda x, y : x ** y

for a in range(-2, 3):
    print(cuadrado(a), end=" ")
    print(potencia(a, dos()))
'''
'''
def imprimirfuncion(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

imprimirfuncion([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
'''

lista1 = [x for x in range(5)]
lista2 = list(map(lambda x : x * x, lista1))
print(lista2)

for x in map(lambda x : x*x,lista2):
    print(x,end=" ")
print()
