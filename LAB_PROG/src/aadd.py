def pegarmax(lista):
        tei = max(lista)
        deish = lista.index(tei)
        return deish
cadeia = []
entrada= [int(x)for x in input().replace('\\n', ' ').split(" ")]
for k in range(0,len(entrada),3):
    cadeia = []
    tamanho = entrada[k]
    remocao = entrada[k+1]
    entrada1 = str(entrada[k+2])            
    for x in entrada1:
        cadeia.append(x)    
    cont= 0    
    zezin = pegarmax(cadeia)
    dedurar = ""
    while len(dedurar) < (tamanho-remocao):        
        if len(cadeia[zezin:])+cont <(tamanho-remocao):
            while len(cadeia[zezin:])+cont <(tamanho-remocao):
                sub = cadeia[:zezin]
                zezin = pegarmax(sub)
            
        else:
            dedurar += cadeia[zezin]
            cadeia = cadeia[(zezin+1):]
            cont+=1
    print(dedurar)
                