


from gettext import find
from pickletools import string1


def misplit(strng):
    #
    try:
        
        palabra = ''
        salida = []
        assert  not strng.isalnum()
        if strng.isspace():
            return salida
        for l in range(len(strng)):
            
            if strng[l] != " " :
                palabra += strng[l]
                #print(l,len(strng)-1)
                if l == (len(strng)-1):
                    salida.append(palabra)
                if palabra =='':
                     continue
            elif strng[l] == " " :
                if palabra =='':
                     continue
                else:
                    salida.append(palabra)
                    palabra = ""
            
                    
            else:
                salida.append(palabra)
                palabra = ""
        
        
    except AssertionError:
        print("ingrese unicamente letras")
    except:
         print("ingrese unicamente letras")    
    return salida
    
            

    


#
print(misplit("Ser ola "))
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
