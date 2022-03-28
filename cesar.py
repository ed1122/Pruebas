# Cifrado César

text = input("Ingresa tu mensaje: ")
cambio = int(input("ingresa valor de cambio: "))
try:
    assert cambio <= 25 and cambio >= 1
    cifrado = ''
    for char in text:
        code = ord(char) + cambio
        if char.isupper():
            if code > ord('Z'):
                code = 64+code-90
            cifrado += chr(code)
        elif char.islower():
            if code > ord('z'):
                code = 96+code-122
            cifrado += chr(code)
        elif not char.isalpha():
            cifrado += char
    print("cifrando:")
    print(cifrado)
        
    
except AssertionError:
    print("valor inválido")
except:
    print("Valor inválido")