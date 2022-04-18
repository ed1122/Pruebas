from os import strerror

'''try:
    fo = open("newText.txt","wt")# nuevo archivo es creado
    for i in range(10):
        s = "línea #"+ str(i+1)+ "\n"
        for ch in s:
            fo.write(ch)
    fo.close()   
    of = open("newText.txt","r")
    print(of.read()) 
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
    '''
import sys

try:
    fo = open('newText.txt','wt')
    for i in range(10):
        fo.write('line #'+ str(i+1)+'\n')
    fo.close()
except IOError as e:
    print("se produjo un error de E/S: ",strerror(e.errno))
    sys.stderr.write("Mensaje de Error")

