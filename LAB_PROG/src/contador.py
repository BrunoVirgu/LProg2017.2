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
        self.__prox = None
        self.__ant = None
        self.__dado = None
    
    def getDado(self):
        return self.__dado
    def setDado(self,novoDado):
        self.__dado = novoDado
    
    def getInicio(self):
        return self.__Inicio  
    def setInicio(self,novoInicio):
        self.__Inicio = novoInicio
    
    
    def getFim(self):
        return self.__Fim 
    def setFim(self,novoFim):
        self.__Fim = novoFim
    
    
    def getProx(self):
        return self.__prox
    def setProx(self,novoProx):
        self.__prox = novoProx
        
    def getAnt(self):
        return self.__ant  
    def setAnt(self,novoAnt):
        self.__ant = novoAnt    
    
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
    
    def InserirNoFinalLista(self,Valor):
        NovoNodo = Valor
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
        


identidade = 0
entrada = int(input())
for i in range(entrada):
    players = Lista()
    DeckDaMesa = Lista()
    entrada2 =  [int(x) for x in input().split(" ")]
    for x in entrada2:
        DeckDaMesa.InserirNoFinal(int(x))#cria o deck da mesa
    while True:#Cria a festa até achar o -1
        pessoas = [int(x) for x in input().split(" ")]
        if pessoas[0] == -1:#acaba a festa
            break
        deish = Lista()#cria um objeto lista
        identidade +=1
        deish.setDado(identidade)
        for c in pessoas:
            deish.InserirNoFinal(c)#insere no final por ser uma fila
        players.InserirNoFinalLista(deish)#adiciona a pessoa na lista de jogadeores
    
    conta = 0
    saida = ""

    while True:
        if len(saida)>0:
            break
        if conta ==1000:
            saida +="0"
        conta+=1
        CartaAtual = DeckDaMesa.getInicio().getDado()#pea a carta atual
        jogador = players.getInicio()
        while True:
            if jogador.verificarVazio():
                saida+=str(jogador.getDado())
                break
            else:
                cartaJogador = jogador.getInicio().getDado()
                if cartaJogador == CartaAtual:
                    jogador.RemoverDoInicio()
                else:
                    rotacionar = jogador.RemoverDoInicio()
                    realocar = jogador.InserirNoFinal(rotacionar)
            if jogador.getProx() == None:
                break
            jogador = jogador.getProx()
        
        Rotacionar = DeckDaMesa.RemoverDoInicio()#tira a carta de cima da mesa
        realocar = DeckDaMesa.InserirNoFinal(Rotacionar)#joga ela pro final
    print(saida)
        
        
        
        
        
        