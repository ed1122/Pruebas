from os import strerror

hist = {}
for let in range(97,123):
    ch = chr(let)
    hist[ch] = 0

try:
    file = open('hist.txt','r', encoding='utf-8')
    contenido = file.read().lower()
    
    for c in contenido:
        if c in hist.keys():
            hist[c]+=1
    
    h_sorted = {}
    sort_keys = sorted(hist, key=hist.get, reverse=True)

    for s in sort_keys:
        h_sorted[s] = hist[s]

    #print("h items")
    #print(h_sorted)

    res = open("hist.hist","wt")
    
    for i in h_sorted.keys():
        if h_sorted[i] > 0:
            print(i,"->",h_sorted[i])
            h = str(i)+" -> "+str(h_sorted[i])+"\n"
            res.write(h)
    
    

    
    file.close()
    res.close()

    file = open('hist.hist','r', encoding='utf-8')
    contenido = file.read()
    print(contenido)


except IOError as e:
    print('No se pudo leer el archivo;',strerror(e.errno) )