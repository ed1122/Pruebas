'''El protocolo iterador es una forma en que un objeto debe comportarse para ajustarse a las reglas impuestas por el contexto de las sentencias for e in. Un objeto conforme al protocolo iterador se llama iterador.

Un iterador debe proporcionar dos métodos:

__iter__() el cual debe devolver el objeto en sí y que se invoca una vez (es necesario para que Python inicie con éxito la iteración).
__next__() el cual debe devolver el siguiente valor (primero, segundo, etc.) de la serie deseada: será invocado por las sentencias for/in para pasar a la siguiente iteración; si no hay más valores a proporcionar, el método deberá lanzar la excepción StopIteration.
¿Suena extraño? De ningúna manera. Mira el ejemplo en el editor.

Hemos creado una clase capaz de iterar a través de los primeros n valores (donde n es un parámetro del constructor) de los números de Fibonacci.

Permítenos recordarte: los números de Fibonacci(Fibi) se definen de la siguiente manera:

Fib1 = 1
Fib2 = 1
Fibi = Fibi-1 + Fibi-2

En otras palabras:

Los primeros dos números de la serie Fibonacci son 1.
Cualquier otro número de Fibonacci es la suma de los dos anteriores (por ejemplo, Fib3 = 2, Fib4 = 3, Fib5 = 5, y así sucesivamente).
Vamos a ver el código:

Líneas 2 a 6: el constructor de la clase imprime un mensaje (lo usaremos para rastrear el comportamiento de la clase), se preparan algunas variables: (__n para almacenar el límite de la serie, __i para rastrear el número actual de la serie Fibonacci, y __p1 junto con __p2 para guardar los dos números anteriores).

Líneas 8 a 10: el método __iter__ está obligado a devolver el objeto iterador en sí mismo; su propósito puede ser un poco ambiguo aquí, pero no hay misterio; trata de imaginar un objeto que no sea un iterador (por ejemplo, es una colección de algunas entidades), pero uno de sus componentes es un iterador capaz de escanear la colección; el método __iter__ debe extraer el iterador y confiarle la ejecución del protocolo de iteración; como puedes ver, el método comienza su acción imprimiendo un mensaje.

Líneas 12 a 21: el método __next__ es responsable de crear la secuencia; es algo largo, pero esto debería hacerlo más legible; primero, imprime un mensaje, luego actualiza el número de valores deseados y, si llega al final de la secuencia, el método interrumpe la iteración al generar la excepción StopIteration; el resto del código es simple y refleja con precisión la definición que te mostramos anteriormente.

Las líneas 23 y 24 hacen uso del iterador.'''
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")        
        return self

    def __next__(self):
        print("__next__")                
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(3):
    print(i)

