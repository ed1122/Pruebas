from random import randrange



def DisplayBoard(board):
    #
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

    for fila in range(len(board[0])):
        print("+-------"*3,"+",sep="")
        print("|       "*4)
        print("|",end="")
        
        
        for col in range(len(board)):
            
            print("   ",board[fila][col],"   |",sep="",end="")
            
        
        print(" ")
        print("|       "*4)
    print("+-------"*3,"+",sep="")
    return board


def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    
    
    casillas=MakeListOfFreeFields(board)
    verif=()
    

    mov=input("Ingrese movimiento: ")
    v=True
    while v:    
        if mov =="1":
            verif=(tuple((0,0)))
        elif mov=="2":
            verif=(tuple((0,1)))
        elif mov=="3":
            verif=(tuple((0,2)))
        elif mov=="4":
            verif=(tuple((1,0)))
        elif mov=="6":
            verif=(tuple((1,2)))
        elif mov=="7":
            verif=(tuple((2,0)))
        elif mov=="8":
            verif=(tuple((2,1)))
        elif mov=="9":
            verif=(tuple((2,2)))
        
        
        if verif not in casillas:
            mov=input("Ingresa otro movimiento casilla no disponible: ")
        else:
            break  
                
    if mov =='1':
        board[0][0]="O"
    elif mov =='2':
        board[0][1]="O"
    elif mov =='3':
        board[0][2]="O"
    elif mov =='4':
        board[1][0]="O"
    elif mov =='6':
        board[1][2]="O"
    elif mov =='7':
        board[2][0]="O"
    elif mov =='8':
        board[2][1]="O"
    elif mov =='9':
        board[2][2]="O"
    return board
    
    
    
    

    
def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    fields=[]
    for fil in range(len(board)):
        for col in range(len(board[fil])):
            if board[fil][col] == "X" or board[fil][col] == "O":
                continue
            else:
                fields.append(tuple((fil,col)))
    
    return fields


def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    #if MakeListOfFreeFields(tablero)!=[]:
        for fil in range(len(board)):
            if board[fil][0] == board[fil][1] == board[fil][2]==sign:
                    print("Felicidades gana: ",sign)
                    return True
                    break
        for colum in range(len(board[0])):
                if board[colum][0] ==  board[colum][1] ==  board[colum][2]==sign :
                            print("Felicidades gana: ",sign)
                            return True
                            break
        if board[0][0] == board[1][1]==board[2][2]==sign:
            print("Felicidades gana: ",sign)
            return True
            
        elif board[0][2] == board[1][1]==board[2][0]==sign:
                    print("Felicidades gana: ",sign)
                    return True
                    
        elif MakeListOfFreeFields(board)==[]:
            print("Es un empate!! ")
            return True
        return False
    #return False
    




def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    verif=()
    casillas=MakeListOfFreeFields(board)
    

    mov=str(randrange(1,10))
    v=True
    while v:    
        if mov =="1":
            verif=(tuple((0,0)))
        elif mov=="2":
            verif=(tuple((0,1)))
        elif mov=="3":
            verif=(tuple((0,2)))
        elif mov=="4":
            verif=(tuple((1,0)))
        elif mov=="6":
            verif=(tuple((1,2)))
        elif mov=="7":
            verif=(tuple((2,0)))
        elif mov=="8":
            verif=(tuple((2,1)))
        elif mov=="9":
            verif=(tuple((2,2)))
        
        
        if verif not in casillas:
            mov=str(randrange(1,10))
        else:
            break     
        
    if mov =='1':
        board[0][0]="X"
    elif mov =='2':
        board[0][1]="X"
    elif mov =='3':
        board[0][2]="X"
    elif mov =='4':
        board[1][0]="X"
    elif mov =='6':
        board[1][2]="X"
    elif mov =='7':
        board[2][0]="X"
    elif mov =='8':
        board[2][1]="X"
    elif mov =='9':
        board[2][2]="X"
    return board
        

#Inicio  de programa

global tablero
tablero=[['1','2','3'],
                ['4','X','6'],
                ['7','8','9']]

inicio = int(input("Igrese 1 para jugar // 0 para salir: "))
if inicio:
    j=True
    gana =False
    DisplayBoard(tablero)
    while j:
        
        if inicio:
                        
            #movimiento de jugador
            print("Turno de jugador")
            EnterMove(tablero)
            DisplayBoard(tablero)
            if VictoryFor(tablero,"O"):
                break
            #movimiento de maquina
            print("Turno de la máquina")
            DrawMove(tablero)
            DisplayBoard(tablero)
            if VictoryFor(tablero,"X"):
                
                break
            
            continue

            
        else:
            j=False
