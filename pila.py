"""
# ENFOQUE PROCEDIMENTAL
pila = []

def push(val):
    pila.append(val)


def pop():
    val = pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
"""


# ENFOQUE ORIENTADO A OBJETOS

class Pila: #define la clase pila
    def __init__(self): #define la funcion del constructor
        #print("!HOLA¡")
        self.__listaPila = []
    
    def getl(self):
        return self.__listaPila

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val

class SumarPila(Pila): #subclase que apunta a superclase Pila
    def __init__(self):
        Pila.__init__(self) #invocando constructor de la superclase es importante
        self.__sum = 0

    def getSuma(self):
        return self.__sum

    #agregando funcionalidad en la subclase
    def push(self,val): 
        self.__sum += val
        Pila.push(self,val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val
    

objetoPila = Pila() # instanciando el objeto

objetoPila.push(3)
#print(len(objetoPila.listaPila)) # no podemos acceder a la variable ya es privada
objetoPila.push(2)
objetoPila.push(1)
print("pila superclase",objetoPila.getl())

# print(objetoPila.pop())
# print(objetoPila.pop())
# print(objetoPila.pop())

objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

print("accediendo a la subclase")

objetoPila = SumarPila() # creando objeto de la subclase

for i in range(5):
    objetoPila.push(i)
print(objetoPila.getSuma())

for i in range(5):
    print(objetoPila.pop())
print("suma",objetoPila.getSuma())

print("pila subclase",objetoPila.getl())

print(objetoPila.__dict__)
print(objetoPila1.__dict__)
print(objetoPila2.__dict__)
