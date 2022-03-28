fech = input("ingrese fecha de nacimiento: ")

try:
    fech = fech.replace(" ","")
    
    if fech == "":
        raise
    l =0
    suma = 0
    while l != 1:
        for n in fech:
            n = int(n)
            suma += n
            
        if len(str(suma)) != 1:
            fech = str(suma)
            suma = 0
        else:
            break
            

    print("El dígito de la vida es: ",suma)
            

except:
    print("Datos no válidos")