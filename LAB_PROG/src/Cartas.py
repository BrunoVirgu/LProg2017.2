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


entrada = int(input())
for i in range(entrada):
    saida = ""
    players = []
    vencedor = []
    DeckDaMesa = Lista()
    entrada2 =  [int(x) for x in input().split(" ")]
    for x in entrada2:
        DeckDaMesa.InserirNoFinal(int(x))#cria o deck da mesa
    
    while True:#Cria a festa até achar o -1
        pessoas = [int(x) for x in input().split(" ")]
        if pessoas[0] == -1:
            break
        deish = Lista()
        for c in pessoas:
            deish.InserirNoFinal(c)
        players.append(deish)
    
    conta = 0
    saida = ""
    while True:                
        if len(saida)>0:
            break
        if conta ==1000:
            saida +="0"
        conta+=1
        CartaAtual = DeckDaMesa.getInicio().getDado()
        for teste in players:
            if teste.verificarVazio():
                saida +=str(players.index(teste)+1)
                break
            else:
                CartaJogador = teste.getInicio().getDado()
                if CartaJogador == CartaAtual:
                    teste.RemoverDoInicio()
                else:
                    rotacionar = teste.RemoverDoInicio()
                    realocar = teste.InserirNoFinal(rotacionar)
                    
                    
    
        
        Rotacionar = DeckDaMesa.RemoverDoInicio()
        realocar = DeckDaMesa.InserirNoFinal(Rotacionar)
        
    print(saida)   
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            