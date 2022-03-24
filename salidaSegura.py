from asyncio.base_subprocess import WriteSubprocessPipeProto
from dis import get_instructions


def readint(prompt, min, max):
    #
    val=True
    while val:
        try:
            n= int(input(prompt))
            if n > min and n <max:
                val=False                
            else:
                print("Error: el valor no está dentro del rango permitido (",min,"...",max,")",sep="")
                
        except ValueError:
            print("Error: entrada incorrecta")
        except KeyboardInterrupt:
            print("Terminando ejecución")
            return 0
            
    return n
    

#

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
