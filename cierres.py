'''from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5) ]
filtered = list(filter(lambda x : x>0 and x%2 ==0,data))
print(data)
print(filtered)
'''
#cierres
'''
def exterior(par):
    loc = par
    x = 12
    def interior():
        
        return loc
    return interior

var = 1
fun = exterior(var)
print(fun())
'''
def crearcierre(par):
    loc = par 
    def potencia(p):
        return p ** loc 
    return potencia

fsqr = crearcierre(2)
fcub = crearcierre(3)

for i in range(5):
    print(i, fsqr(i),fcub(i))