grupo = {}

while True:
    nombre = input("Ingrese el nombre del estudiante (exit para detener):")
    if nombre=='exit':
        break
    calif = int(input("Ingresa la calificacion del alumno (0-10):"))

    if nombre in grupo:
        grupo[nombre]+= (calif,)
    else:
        grupo[nombre]=(calif,)
for nombre in grupo:
    sum=0
    contador=0
    for calif in grupo[nombre]:
        sum+=calif
        contador +=1
    print(nombre,":",sum/contador)


print(grupo) 