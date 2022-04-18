from os import strerror

data =  bytearray(10)
#databr = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open("file.bin","wb")
    bf.write(data)
    bf.close()

    br =  open("file.bin","rb")
    br.readinto(data)
    br.close()

    for b in data:
        print(hex(b),end=" ")

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


file = open("file.bin","rb")
print(file.read())

print("ahora con read()")
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

print("especificando caracteres")


try :
    bf= open("file.bin",'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b),end=' ')
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

'''los primeros cinco bytes del archivo han sido leídos por el código;
 los siguientes 5 están esperando a sser procesados'''