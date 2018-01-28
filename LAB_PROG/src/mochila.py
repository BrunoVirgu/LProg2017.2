def distancia(s1, s2):
    if len(s1) < len(s2):
        return distancia(s2, s1)

    if len(s2) == 0:
        return len(s1)

    anterior = range(len(s2) + 1)#o anterior é o tamanho da menor string
    for i, k in enumerate(s1):#for citando e enumerando
        atual = [i + 1]
        for j, l in enumerate(s2):#segundo for
            inserir = anterior[j + 1] + 1#regra de inserir
            deletar = atual[j] + 1#regra de deletar       
            substituir = anterior[j] + (k != l)#regra de substituir se for diferente
            atual.append(min(inserir, deletar, substituir))
        anterior = atual
    
    return anterior[-1]

entrada = [int(x) for x in input().split(" ")]
um=[]
dois=[]
for i in range(entrada[0]):
    certas = input()
    um.append(certas)
for i in range(entrada[1]):
    zub = input()
    dois.append(zub)

analise=[]
for i in um:
    for k in dois:
            analise.append([k,i])
        

analisefinal=[]
for i in analise:
    tomb = distancia(i[0], i[1])
    if tomb <=2 and tomb >=-2:
        analisefinal.append(i)

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
            