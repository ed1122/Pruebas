'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
from os import strerror
'''
try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

'''
'''
try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        #ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
'''
#leyendo por líneas

'''try:
    ccnt = lcnt = 0
    s = open("text.txt","r")
    line = s.readline()
    while line != "":
        lcnt +=1
        for ch in line:
            print(ch,end="")
            ccnt +=1
        line = s.readline()
    s.close()
    print("\n\nCaracteres en el archivo: ",ccnt)
    print("Líneas en el archivo: ",lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ",strerror(e.errno))'''


#readlines()

try:
    ccnt = lcnt= 0
    s = open("text.txt", "rt")
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines :
            lcnt +=1
            for ch in line:
                print(ch,end="")
                ccnt+=1
        lines = s.readlines(10)
    #s.close()
    print("\n\nCaracteres en el archivo sin invocar close: ",ccnt)
    print("Lineas en el archivo:  ",lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ",strerror(e.errno))

#invocando close() automáticamente
'''
try:
    ccnt = lcnt = 0
    for line in open("text.txt","rt"):
        lcnt += 1
        for ch in line:
            print(ch,end="")
            ccnt +=1
    print("\n\nCaracteres en el archivo: ",ccnt)
    print("Líneas en el archivo: ",lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ",strerror(e.errno))'''