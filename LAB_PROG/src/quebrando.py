def pegarmax(lista):
        tei = max(lista)
        deish = lista.index(tei)
        return deish
zenti = []

while True:
    try:
        
        cadeia = []
        entrada= input()
        
        entrada = [int(x) for x in entrada.split(" ")]
        entrada1= input()
        if entrada1 == "":
            entrada1= input()
        for x in entrada1:
            cadeia.append(x)
            
        cadeia = []
        tamanho = entrada[0]
        remocao = entrada[1]
                  
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
    except:
        break
