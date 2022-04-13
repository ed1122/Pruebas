'''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
from os import strerror

try:
    cnt = 0
    s = open("text.txt", "rt", encoding="utf-8")
    ch = s.read(1)
    while ch != "":
        print(ch, end="")
        cnt +=1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo:",cnt)
except IOError as e:
    print("Se produjo un error de E/S: ",strerror(e.errno))