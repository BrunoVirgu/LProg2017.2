def sub_seq(x,y):
    tamanho1 = len(x)
    tamanho2 = len(y)
    gerarmatriz = [[0] * (tamanho2 + 1) for _ in range(tamanho1 + 1)]
    for i in range(1,tamanho1+1):
        for j in range(1,tamanho2+1):
            if x[i -1] == y[j -1]:
                gerarmatriz[i][j] = gerarmatriz[i-1][j-1] + 1
            else:
                gerarmatriz[i][j] = max(gerarmatriz[i][j-1], gerarmatriz[i-1][j])
    return gerarmatriz[tamanho1][tamanho2]

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
        if len(i)-len(k)>=0 and len(i)-len(k) <=2:
            analise.append([k,i])
        if len(i)-len(k)<0 and len(i)-len(k) >=-2:
            analise.append([k,i])

for i in analise:
    str = ""
    tessalia = len(i[0])
    maria = len(i[1])   
    if tessalia >= maria:
        for u in i[0]:
            if u not in i[1]:
                str+=u               
        i.append(str)        
    else:
        for u in i[1]:
            if u not in i[0]:
                str+= u               
        i.append(str)

analisecompleta = []
for i in analise:
    zero = len(i[2])
    if zero<=2:
        analisecompleta.append(i)
jj = []
for i in analisecompleta:
    cabeca = sub_seq(i[0], i[1])
    interagir = max(len(i[0]),len(i[1]))
    fim = intergrar = cabeca
    if (interagir - cabeca) >= 0 and (interagir - cabeca) <=2:
        i.append(cabeca)
        jj.append(i)
print(jj)  
for i in dois:
    saida = ""
    for j in jj:
        if j[0] ==i:
            saida = saida + j[1] + " "
    if saida =="":
        print(" ")
    else:
        print(saida)