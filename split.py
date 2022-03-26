


from gettext import find


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
                            
            
            elif  strng[l] == " " :
                if palabra =='':
                     continue
                else:
                    salida.append(palabra)
                
            elif strng[l] == "":
                if palabra ==' ':
                     continue
                else:
                    salida.append(palabra)
                    
            else:
                palabra = ""
        
    except AssertionError:
        print("ingrese unicamente letras")
    except:
         print("ingrese unicamente letras")    
    return salida
    
            

    


#
print(misplit("Ser ola q1"))
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(1))