class nodo():
    def __init__(self,dado):
        self.__prox = None
        self.__ant = None
        self.__dado = dado
    
    def getDado(self):
        return self.__dado
    def setDado(self,novoDado):
        self.__dado = novoDado
    
    def getProx(self):
        return self.__prox
    def setProx(self,novoProx):
        self.__prox = novoProx
        
    def getAnt(self):
        return self.__ant  
    def setAnt(self,novoAnt):
        self.__ant = novoAnt
        
        
class Lista():
    def __init__(self,):
        self.__Inicio = None
        self.__Fim= None
    
    def getInicio(self):
        return self.__Inicio  
    def setInicio(self,novoInicio):
        self.__Inicio = novoInicio
    
    
    def getFim(self):
        return self.__Fim 
    def setFim(self,novoFim):
        self.__Fim = novoFim
        
    def verificarVazio(self):
        Vazio = False
        if self.getInicio() == None:
            Vazio = True
        return Vazio
  
    def printarLista(self):
        if self.verificarVazio():
            return "Vazia"
        
        nodoAtual = self.__Inicio
        string = "A lista:"
        while nodoAtual is not None:
            string += str(nodoAtual.getDado())+ " "
            nodoAtual = nodoAtual.getProx()
        return string
           
    def InserirNoComeco(self,Valor):
        NovoNodo = nodo(Valor)#cria um novo nodo
        if self.verificarVazio():
            self.setInicio(NovoNodo)
            self.setFim(NovoNodo)
        else:
            self.getInicio().setAnt(NovoNodo)
            NovoNodo.setProx(self.getInicio())
            self.setInicio(NovoNodo)
            
    def InserirNoFinal(self,Valor):
        NovoNodo = nodo(Valor)
        if self.verificarVazio():
            self.setInicio(NovoNodo)
            self.setFim(NovoNodo)
        else:
            NovoNodo.setAnt(self.getFim())
            self.getFim().setProx(NovoNodo)
            self.setFim(NovoNodo)
    
    
    def RemoverDoFim(self,):
        if self.verificarVazio():
            return print("erro lista vazia")
        valor = self.getFim().getDado()
        if self.getFim() == self.getInicio():
            self.setInicio(None)
            self.setFim(None)
        NodoAtual = self.getInicio()
        while NodoAtual is not self.getFim():
            NodoAtual = NodoAtual.getProx()
        remover = NodoAtual.getAnt()
        remover.setProx(None)
        self.setFim(remover)
        return print ("O valor removido foi: %s" %(valor) )
    
    
    def RemoverDoInicio(self):
        if self.verificarVazio():
            return None
        valor = self.getInicio().getDado()
        if self.getFim() == self.getInicio():
            self.setInicio(None)
            self.setFim(None)
        else:
            reapontar = self.getInicio().getProx()
            reapontar.setAnt(None)
            self.setInicio(reapontar)
        return valor
        
            
    def inverter(self):
        aux = self.getInicio()
        self.setInicio(self.getFim())
        self.setFim(aux)
        aux = self.getInicio()
        while aux.getAnt() is not None:
            aux2 = aux.getAnt()
            aux3 = aux.getProx()
            aux.setAnt(aux3)
            aux.setProx(aux2)
            aux = aux2
        aux.setAnt(aux.getProx())        
        aux.setProx(None)  
        
        
class Pilha(Lista):
    
    def colocar(self,dado):
        self.InserirNoComeco(dado)
    
    def tirar(self):
        self.RemoverDoInicio(3)
           
class Fila(Lista):
    
    def InserirNoFim(self,dado):
        self.InserirNoFinal(dado)
        
    def RemoverDoComeco(self):
        self.RemoverDoComeco()


entrada = int(input())
for casos in range(entrada):
    print("Caso %d:" %(casos+1))
    entradaCasos = int(input())
    Normal = Lista()
    Preferecia = Lista()
    for comandos in range(entradaCasos):
        teste = input()
        if teste[0] == "f":
            Normal.InserirNoFinal(teste[2:])
        elif teste[0] == "p":
            Preferecia.InserirNoFinal(teste[2:])
        elif teste[0] == "A":
            if Normal.verificarVazio():
                if Preferecia.verificarVazio():
                    pass
                else:
                    Preferecia.RemoverDoInicio()
            else:
                Normal.RemoverDoInicio()
        elif teste[0] == "B":
            if Preferecia.verificarVazio():
                if Normal.verificarVazio():
                    pass
                else:
                    Normal.RemoverDoInicio()
            else:
                Preferecia.RemoverDoInicio()
        elif teste[0] == "I":
            if Normal.verificarVazio():
                PrimeirodafilaA = "0"
            else:
                PrimeirodafilaA = Normal.getInicio().getDado()
            if Preferecia.verificarVazio():
                primeiroFilaB = "0"
            else:
                primeiroFilaB = Preferecia.getInicio().getDado()
            
            saida = str(PrimeirodafilaA) + " " + str(primeiroFilaB)
            print(saida)
                    