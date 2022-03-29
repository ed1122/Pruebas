from operator import length_hint


word = input("Ingrese palabra: ")
ch = input("Ingrese Cadena: ")
cont = 0
for lett in word:
    if lett in ch:
        cont +=1
        continue
    else:
        break

if cont == len(word):
    print("Si")
else:
    print("No")