'''Hemos puesto el iterador Fib dentro de otra clase (podemos decir que lo hemos compuesto dentro de la clase Class). Se instancia junto con el objeto de Class.

El objeto de la clase se puede usar como un iterador cuando (y solo cuando) responde positivamente a la invocación __iter__ - esta clase puede hacerlo, y si se invoca de esta manera, proporciona un objeto capaz de obedecer el protocolo de iteración.

Es por eso que la salida del código es la misma que anteriormente, aunque el objeto de la clase Fib no se usa explícitamente dentro del contexto del bucle for.'''
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;

object = Class(8)

for i in object:
    print(i)