class Times():
    def __init__(self,numero):
        self.__numero = numero
        self.__ouro = 0
        self.__prata = 0
        self.__bronze = 0
        self.__total = 0
    
    def getNumero(self):
        return self.__numero
    
    def getouro(self):
        return self.__ouro
    def setouro(self):
        self.__ouro+=1
    
    def getPrata(self):
        return self.__prata
    def setPrata(self):
        self.__prata+=1
        
    def getBronze(self):
        return self.__bronze
    def setBronze(self):
        self.__bronze+=1

    def pesarO(self):
        self.__ouro *=1000
    def pesarP(self):
        self.__prata*=100
    def pesarB(self):
        self.__bronze*=1
    def gettotal(self):
        return self.__total
    def settotal(self):
        self.__total= self.__bronze+self.__prata+self.__ouro

entrada = [int(x) for x in input().split(" ")]
ListaTimes=[]
for i in range(1,entrada[0]+1):
    TimeOO = Times(i)
    ListaTimes.append(TimeOO)
for j in range(entrada[1]):
    modalidade = [int(x) for x in input().split(" ")]
    ouro1=modalidade[0]
    prata1= modalidade[1]
    bronze1 = modalidade[2]
    ListaTimes[ouro1-1].setouro()
    ListaTimes[prata1-1].setPrata()
    ListaTimes[prata1-1].setBronze()

for i in ListaTimes:
    i.pesarO()
    i.pesarP()
    i.pesarB()
    i.settotal()
    print(i.gettotal)

    
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]#direita
        righthalf = alist[mid:]#esquerda

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].gettotal() > righthalf[j].gettotal():
                alist[k]=lefthalf[i]
                i=i+1
            elif lefthalf[i].gettotal() == righthalf[j].gettotal():
                teste = min(lefthalf[i].getNumero(),righthalf[j].getNumero())
                if teste== lefthalf[i].getNumero():
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                j=j+1
                    
                    
                
                
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = ListaTimes
saida = ""
mergeSort(alist)
for i in alist:
    print(i.getNumero())
