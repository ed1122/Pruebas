from dataclasses import replace


text = input("Ingrese Frase: ")

pal = text.lower().replace(" ","")
cad1, cad2 = "",""
if pal != "":
    if len(pal) %2 == 0:
        long = len(pal)//2
        for l in range(long):
            cad1 += pal[l] 
        for r in range(len(pal)-1,long-1,-1):
            
            cad2 += pal[r]
        
    elif len(pal) %2 != 0:
        long = len(pal)//2
        for l in range(long+1):
            cad1 += pal[l] 
        for r in range(len(pal)-1,long-1,-1):
            
            cad2 += pal[r]
    if cad1 == cad2:
        print("Es palindomo")
    else:
        print("No es palindromo")

else:
    print("No es palindromo")



