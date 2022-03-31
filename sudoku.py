def sudoku():
    data = []
    try:
        c = 0    
        while c <9:
            fila = input("ingrese datos:")
            if fila.isalnum() and len(fila) == 9:
                c +=1 
                data.append(fila)
                continue
            else:
                print("datos no válidos")
        print(data)
    except:
        print("datos no válidos")
    
    return valida(data)
    
def valida(lista):
    
    for el in range(len(lista)):
        rep = []
        for d in range(len(lista[el])):
            if lista[el][d] in rep:
                return "no sudoku"
                
            else:
                rep += lista[el][d]

    for d in range(len(lista[0])):
        rep = []
        for el in range (len(lista)):
            if lista[el][d] in rep:
                return "No sudoku"
            else:
                rep += lista[el][d]
                
    
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = [],[],[],[],[],[],[],[],[]
    for el in range(len(lista)):
                
        for d in range(len(lista[el])):
            if el < 3 and d <3:
                if lista[el][d] in c1:
                    return "No sudoku"
                else:
                    c1 += lista[el][d]
            
            if el < 6 and el >2 and d <3:
                if lista[el][d] in c2:
                    return "No sudoku"
                else:
                    c2 += lista[el][d]
            if el < 9 and el >5 and d <3:
                if lista[el][d] in c3:
                    return "No sudoku"
                else:
                    c3 += lista[el][d]
            
            if el < 3 and d >2 and d <6:
                if lista[el][d] in c4:
                    return "No sudoku"
                else:
                    c4 += lista[el][d]

            if el < 6 and el >2 and d >2 and d <6:
                if lista[el][d] in c5:
                    return "No sudoku"
                else:
                    c5 += lista[el][d]

            if el < 9 and el >5 and d >2 and d <6:
                if lista[el][d] in c6:
                    return "No sudoku"
                else:
                    c6 += lista[el][d]
            
            if el < 3 and d >5 and d <9:
                if lista[el][d] in c7:
                    return "No sudoku"
                else:
                    c7 += lista[el][d]

            if el < 6 and el > 2 and d >5 and d <9:
                if lista[el][d] in c8:
                    return "No sudoku"
                else:
                    c8 += lista[el][d]
            
            if el < 9 and el > 5 and d >5 and d <9:
                if lista[el][d] in c9:
                    return "No sudoku"
                else:
                    c9 += lista[el][d]
    return "Sudoku Válido"





print(sudoku())
lp = ['295743861',
      '431865927',
      '876192543',
      '387459216',
      '612387495',
      '549216738',
      '763524189',
      '928671354',
      '154938672']

# lp = ['123',
#       '312',
#       '231']
#print(valida(lp))