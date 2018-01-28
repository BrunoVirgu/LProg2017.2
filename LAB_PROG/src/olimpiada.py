
def quicksort(l2,l1,l3,A,p,r):
    if p < r:
        q = partition(l2,l1,l3,A,p,r)
        quicksort(l2,l1,l3,A, p,q-1)
        quicksort(l2,l1,l3,A,p+1,r)
        
def partition(l2,l1,l3,a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] >=x:
            i = i+1
            a[i],a[j] = a[j],a[i]
            l2[i],l2[j] =l2[j],l2[i]
            l3[i],l3[j] =l3[j],l3[i]
            l1[i],l1[j] =l1[j],l1[i]
    a[i+1],a[r] = a[r],a[i+1]
    l2[i+1],l2[r] = l2[r],l2[i+1]
    l1[i+1],l1[r] = l1[r],l1[i+1]
    l3[i+1],l3[r] = l3[r],l3[i+1]
    
    return i+1    

entrada = [int(x) for x in input().split(" ")]
Times = []
ouro=[]
prata=[]
bronze=[]
for i in range(1,entrada[0]+1):
    Times.append(i)
    ouro.append(0)
    prata.append(0)
    bronze.append(0)
for j in range(entrada[1]):
    modalidade = [int(x) for x in input().split(" ")]
    ouro1=modalidade[0]
    prata1= modalidade[1]
    bronze1 = modalidade[2]   
    ouro[ouro1-1] +=1
    prata[prata1-1]+=1
    bronze[bronze1-1] +=1

      
def destruir(ouro,prata,bronze,Times):
    saida = "" 
    while True:
        if len(Times) == 0:
            break       
        t = quicksort(prata, bronze, Times, ouro, 0, len(ouro)-1)
        maior = ouro[0]
        teste =0
        for i in ouro:
            if i == maior:
                teste+=1
        if teste == 1:
            saida = saida + str(Times[0]) + " "
            Times = Times[1:]
            ouro = ouro[1:]
            prata = prata[1:]
            bronze=bronze[1:]
                 
        else:
            j = quicksort(ouro[0:teste], Times[0:teste], bronze[0:teste], prata[0:teste], 0, len(prata[0:teste])-1)
            maior1 = prata[0]
            teste1 = 0
            for i in prata[0:teste]:
                if i == maior1:
                    teste1+=1
            if teste1 ==1:
                saida = saida + str(Times[0]) + " "
                Times = Times[1:]
                ouro = ouro[1:]
                prata = prata[1:]
                bronze=bronze[1:]
            else:
                k = quicksort(ouro[0:teste1], Times[0:teste1], prata[0:teste], bronze[0:teste1], 0, len(bronze[0:teste1])-1)
                maior2 = bronze[0]
                teste2 = 0
                for i in bronze[0:teste1]:
                    if i == maior2:
                        teste2+=1
                if teste2 ==1:
                    saida = saida + str(Times[0]) + " "
                    Times = Times[1:]
                    ouro = ouro[1:]
                    prata = prata[1:]
                    bronze=bronze[1:]
                    
                else:
                    u =  quicksort(ouro[0:teste1], bronze, prata[0:teste], Times[0:teste1], 0, len(Times[0:teste1])-1)
                    cont = 0
                    while cont!= teste1:
                        saida = saida + str(Times[0]) + " "
                        Times = Times[1:]
                        ouro = ouro[1:]
                        prata = prata[1:]
                        bronze=bronze[1:]
                        cont+=1                       
    return print(saida[:-1]) 
kappa = destruir(ouro, prata, bronze, Times)

