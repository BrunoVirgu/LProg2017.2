entrada = [int(x) for x in input().split(" ")]
JuvenalsFarmy = {}
linha = entrada[0]
coluna = entrada[1]

totalOvelhas = 0
totalLobos = 0
for x in range(linha):
    entrada2 =  input()
    for j,k in enumerate(entrada2):
        if k == "v":
            totalLobos+=1
        if k == "k":
            totalOvelhas+=1
        JuvenalsFarmy[(x,j)]= k

def Acharvzinho(matriz, MLinha, NColuna, i,j):
    PROXIMOOS = []
    if i > 0 and matriz[(i-1,j)] != '#' and i > 0 and matriz[(i-1,j)] != 'X' :#cima
        PROXIMOOS.append ((i-1, j))
    if i+1 < MLinha and matriz[(i+1,j)] != '#' and matriz[(i+1,j)] != 'X':#baixo
        PROXIMOOS.append ((i+1, j))
    if j > 0 and matriz[(i,j-1)] != '#' and matriz[(i,j-1)] != 'X':#esquerda
        PROXIMOOS.append ((i, j-1))
    if j+1 < NColuna and matriz[(i,j+1)] != '#' and matriz[(i,j+1)] != 'X' :#direita
        PROXIMOOS.append ((i, j+1))
    return PROXIMOOS


for i in range(linha):    
    for j in range(coluna):
        pasto = []
        if JuvenalsFarmy[(i,j)] != "#"and JuvenalsFarmy[(i,j)] != "X":
            Teste = Acharvzinho(JuvenalsFarmy, linha, coluna, i, j)
            if len(Teste)>0:
                for o in Teste:
                    pasto.append(o)
                    for p in pasto:
                        k = Acharvzinho(JuvenalsFarmy, linha, coluna, p[0], p[1])
                        for u in k:
                            if not u in pasto:
                                pasto.append(u)
        lobopasto = 0
        ovelhapasto = 0
        if len(pasto)>1:
            print(pasto)
            for an in pasto:
                if JuvenalsFarmy[(an[0],an[1])] == "v":
                    lobopasto+=1
                    JuvenalsFarmy[(an[0],an[1])] = "X"
                elif JuvenalsFarmy[(an[0],an[1])] == "k":
                    ovelhapasto +=1
                    JuvenalsFarmy[(an[0],an[1])] = "X"
                else:
                    JuvenalsFarmy[(an[0],an[1])] = "X"
        if ovelhapasto>lobopasto:
            totalLobos-=lobopasto
        else:
            totalOvelhas-=ovelhapasto
print(totalOvelhas,totalLobos)
                
            
            
            
            
        