def vencedor(lista):
    
    for x in lista:
        numero = x.find(" ")
        a = int(x[numero+1:])
        b = a - len(lista)
        while True:
            if a % 2 == 0:
                while True:
                    if b<= len(lista):
                       
                        pos = lista.index(lista[b-1])
                        n = lista.pop(b-1)
                        numero = n.find(" ")
                        a = int(n[numero+1:])
                        
                        b = a - pos
                    
                    
                        
                        break
                    else:
                        b = b - len(lista)
            else:
                while True:
                    
                    if b<= len(lista):
                        pos = lista.index(lista[b-1])
                        lista.reverse()
                        n = lista.pop(b-1)
                        lista.reverse()
                        numero = n.find(" ")
                        a = int(n[numero+1:])
                        b = a - pos
                                        
                        
                        
                        break
                    else:
                        b = b - len(lista)
            if len(lista) == 1:
                break
    return lista[0]


lista2 = []
while True:
    
    entrada = input()
    if entrada=="0":
        break
    else:
        lista = []
        for x in range(int(entrada)):
            
            lista.append(input())
        lista2.append(lista)
            

for x in lista2:
    a = vencedor(x)
    n = a.find(" ")
    
    print("Vencerdor(a): %s" % a[0:n])