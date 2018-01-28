def distancia_de_edição(x,y):
    matriz = {}
    x = ' ' + x#adiciona espaço em brando para facilitar construir a tabela
    y = ' ' + y
    #crianco caso base
    for i in range(len(x)):
        matriz[(i,0)] = i
    for j in range(len(y)):
        matriz[(0,j)] = j
    #preechendo com as regras
    for j in range(1,len(y)):
        for i in range(1,len(x)):
            if x[i] == y[j]:
                matriz[(i,j)] = matriz[(i-1,j-1)]
            else:
                adicao = matriz[(i,j-1)]
                remocao = matriz[(i-1,j)]
                modificacao = matriz[(i-1,j-1)]
                matriz[(i,j)] =  min(adicao,remocao,modificacao)+1
    return print(matriz[len(x)-1,len(y)-1])
                
   
            
cu = distancia_de_edição("cu", "tube")    
            
            
            
for i in dois:
    saida = ""
    for j in jj:
        if j[0] ==i:
            saida = saida + j[1] + " "
    if saida =="":
        print(" ")
    else:
        print(saida)            
            



for i in dois:
    saida = []
    for j in analisefinal:
        if j[0] ==i:
            if not j[1] in saida:
                saida.append(j[1])
    if len(saida) == 0:
        print(" ")
    else:
        strl =""
        for i in saida:
            strl = strl + i + " "
        print(strl)          
            
            
            
            
            
            
            
            
            