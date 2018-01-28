import time
def programa():
    entrada = [int(x) for x in input().split(" ")]
    dic = {}
    winner = ""
    for x in range(1,entrada[0]+1):
        dic[x] = [0,0,0]
    for j in range(entrada[1]):
        modadalidade = [int(x) for x in input().split(" ")]
        ouro = modadalidade[0]
        prata = modadalidade[1]
        bronze = modadalidade[2]
        dic[ouro][0]+=1
        dic[prata][1]+=1
        dic[bronze][2]+=1
    
    
    def getOuro(dic):
        maior = 0
        lista = []
        for teste1 in dic:
            if dic[teste1][0]> maior:
                maior = dic[teste1][0]
                lista= []
                lista.insert(0,teste1)
            elif dic[teste1][0] == maior:
                lista.append(teste1)
        return lista
    
    def getPrata(listaEmpate,dic):
        maior1 = 0
        listaPrata = []
        for x in listaEmpate:
            if dic[x][1] > maior1:
                maior1 = dic[x][1]
                listaPrata = []
                listaPrata.insert(0,x)
            elif dic[x][1] == maior1:
                listaPrata.append(x)
        return listaPrata
    
    def getBronze(listaEmpate,dic):
        maior1 = 0
        listaPrata = []
        for x in listaEmpate:
            if dic[x][2] > maior1:
                maior1 = dic[x][2]
                listaPrata = []
                listaPrata.insert(0,x)
            elif dic[x][2] == maior1:                
                listaPrata.append(x)
        return listaPrata
        
    def quicksort(A,p,r):
        if p < r:
            q = partition(A,p,r)
            quicksort(A, p,q-1)
            quicksort(A,p+1,r)
            
    def partition(a,p,r):
        x = a[r]
        i = p-1
        for j in range(p,r):
            if a[j] <=x:
                i = i+1
                a[i],a[j] = a[j],a[i]
        a[i+1],a[r] = a[r],a[i+1]
        
        return i+1    
            
    while len(dic) is not 0:
        teste = getOuro(dic)
        if len(teste) >1:
            teste2 = getPrata(teste, dic)            
            if len(teste2)>1:
                teste3 = getBronze(teste2, dic)     
                if len(teste3) >1:
                    a = quicksort(teste3, 0,len(teste3)-1)
                    for i in teste3:
                        winner = winner + str(i) + " "
                        del dic[i]
                else:
                    chave = teste3[0]
                    winner = winner + str(chave) + " "
                    del dic[chave]        
            
            else:
                chave = teste2[0]
                winner = winner + str(chave) + " "
                del dic[chave]
                
        else:
            chave = teste[0]
            winner = winner + str(chave) + " "
            del dic[chave]
            
                
         
    return print(winner)

inicio = time.time()
tava = programa()
fim = time.time()
print(fim-inicio)