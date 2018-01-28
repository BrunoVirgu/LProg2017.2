entrada = [int(x) for x in input().split(" ")]
MAR = {}
linha = entrada[0]
coluna = entrada[1]


for x in range(linha):
    entrada2 =  input()
    for j,k in enumerate(entrada2):
        MAR[(x,j)]= k

def Acharvzinho(matriz, MLinha, NColuna, i,j):
    PROXIMOOS = []
    if i > 0 and matriz[(i-1,j)] != ".": #cima
        PROXIMOOS.append ((i-1, j))
    if i+1 < MLinha and matriz[(i+1,j)] != ".":#baixo
        PROXIMOOS.append ((i+1, j))
    if j > 0 and matriz[(i,j-1)] != '.':
        PROXIMOOS.append ((i, j-1))
    if j+1 < NColuna and matriz[(i,j+1)] != ".":#direita
        PROXIMOOS.append ((i, j+1))
    return PROXIMOOS

finalfight=[]
tamanhos =[]
for i in range(linha):    
    for j in range(coluna):
        navio = []
        if MAR[(i,j)] != ".":
            navio.append((i,j))
            MAR[(i,j)] = "."
            Teste = Acharvzinho(MAR, linha, coluna, i, j)
            if len(Teste)>0:
                for o in Teste:
                    navio.append(o)
                    MAR[o] = "."
                    for p in navio:
                        k = Acharvzinho(MAR, linha, coluna, p[0], p[1])
                        for u in k:
                            if not u in navio:
                                navio.append(u)
                                MAR[u] = "."
    
        if len(navio)>0:
            finalfight.append(navio)
for i in finalfight:
    tamanhos.append(len(i))
    
destruidos = 0        
qt_tiros = int(input())
for i in range(qt_tiros):
    tiro = [int(x) for x in input().split(" ")]        
    tiro1 = (tiro[0]-1,tiro[1]-1)  
    for i in finalfight:
        for k in i:
            if k == tiro1:
                lugar=finalfight.index(i)
                tamanhos[lugar]-=1
                
                

print(tamanhos.count(0))
            
            
            
            
        