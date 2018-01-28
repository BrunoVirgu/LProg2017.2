
class Times():
    def __init__(self,numero):
        self.__numero = numero
        self.__ouro = 0
        self.__prata = 0
        self.__bronze = 0
    
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
        
entrada = [int(x) for x in input().split(" ")]
ListaTimes=[]
cont=1
for i in range(entrada[0]):
    TimeOO = Times(cont)
    ListaTimes.append(TimeOO)
    cont+=1
for j in range(entrada[1]):
    modalidade = [int(x) for x in input().split(" ")]
    ouro = modalidade[0]
    prata=modalidade[1]
    bronze = modalidade[2]
    ListaTimes[ouro-1].setouro()
    ListaTimes[prata-1].setPrata()
    ListaTimes[bronze-1].setBronze()

def vaitrocar(A,B):
    if A.getouro()>B.getouro():
        return False
    elif A.getouro()<B.getouro():
        return True
    else:
        if A.getPrata()> B.getPrata():
            return False
        elif A.getPrata() < B.getPrata():
            return True
        else:
            if A.getBronze()>B.getBronze():
                return False
            elif A.getBronze()<B.getBronze():
                return True
            else:
                return A.getNumero()>=B.getNumero()

def verificador(ListaTimes):
    ListaStop = []
    indice=0
    while True:
        if len(ListaTimes)-indice==1:
            indice=0
            ListaStop.append("N")
            if ListaStop.count("N")> ListaStop.count("S"):
                break
        if vaitrocar(ListaTimes[indice], ListaTimes[indice+1]):
            ListaTimes[indice], ListaTimes[indice+1] = ListaTimes[indice+1], ListaTimes[indice]
            indice+=1
            ListaStop.append("S")
            
        else:
            indice+=1
    return ListaTimes
saida = ""
k = verificador(ListaTimes)
for i in k:
    saida+=str(i.getNumero())+ " "
print(saida[:-1])
    
    