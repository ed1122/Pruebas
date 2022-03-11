def lbakg(lb):
    return lb* 0.45359237

def piepulgam(pie=0,pulgada=0.0):
    return pie * 0.3048 + pulgada * 0.0254

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
        peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2


print(imc(52.5, 1.65))
print(piepulgam(6))
print(imc(lbakg(176),piepulgam(5,7)))