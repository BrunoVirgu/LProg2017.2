    def distancia(x,y):
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
    return(matriz[len(x)-1,len(y)-1])

entrada = [int(x) for x in input().split(" ")]
dicionario=[]
for i in range(entrada[0]):
    certas = input()
    dicionario.append(certas)
for i in range(entrada[1]):
    zub = input()
    saida = ""
    for k in dicionario:
        zuzu = len(zub)- len(k)
        if zuzu <=2 and zuzu>=-2:
            z = distancia(k, zub)
            if z<=2:
                saida = saida+k+" "
    if saida =="":
        print(" ")
    else:
        print(saida)       

            