phr1 = input("Ingrese frase 1: ")
phr2 = input("Ingrese frase 2: ")

f1 = phr1.lower().replace(" ","")

f2 = phr2.lower().replace(" ","")

if sorted(f1) == sorted(f2):
    print("Anagramas")
else:
    print("No son anagramas")


in_list = ['casa','roma','perla','saca','mora','regla']
list_anagram = []

for i in range(0, len(in_list) - 1):
    if sorted(in_list[i]) not in list_anagram:
        for j in range(i + 1, len(in_list)):
            isanagram = (sorted(in_list[i]) == sorted(in_list[j]))
            if isanagram:
                list_anagram.append(sorted(in_list[i]))
                print(f'{in_list[i]} = {in_list[j]} Is an ANAGRAM')
            else:
                print(f'{in_list[i]} != {in_list[j]} Is Not an ANAGRAM')