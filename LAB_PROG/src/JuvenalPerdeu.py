
class TreeNode():
    def __init__(self,dado):
        self.__dado = dado
        self.__left = None
        self.__right = None
        self.__pai = None
        
    def getDado(self):
        return self.__dado
    def setDado(self,novodado):
        self.__dado = novodado
    
    
    def getFilhoEsquerdo(self):
        return self.__left
    def setFilhoEsquerdo(self,novoFilho):
        self.__left = novoFilho
    
    def getFilhoDireito(self):
        return self.__right
    def setFilhoDireito(self,Novofilho):
        self.__right = Novofilho
    
    def getPai(self):
        return self.__pai
    def setPai(self,novoPai):
        self.__pai = novoPai
    
class BinaryTree():
    def __init__(self):
        self.__print = ""
        self.__raiz = None
        self.__pre = 0
        self.__kappa = 0
    
    def setpre(self,novopre):
        self.__pre=novopre
    def getpre(self):
        return self.__pre
    def resetpre(self):
        self.__pre = 0
    
    def getprint(self):
        return self.__print
    
    def resetprint(self):
        self.__print = ""
    
    def getRaiz(self):
        return self.__raiz
    def setRaiz(self,novaRaiz):
        self.__raiz = novaRaiz
        
    def isEmpty(self):
        if self.getRaiz() == None:
            return True
        else:
            return False
    
    def isLeft(self,nodo):
        q = nodo.getPai()
        if q == None:
            return False
        if q.getFilhoEsquerdo() == nodo:
            return True
        return False
    def isRight(self,nodo):
        q = nodo.getPai()
        if q == None:
            return False
        if q.getFilhoDireito() == nodo:
            return True
        return False
    
    def brother(self,nodo):
        if nodo.getPai() == None:
            return False
        if self.isLeft(nodo):
            return nodo.getPai().getFilhoDireito()
        return nodo.getPai().getFilhoEsquerdo()
    
    def Tree_search(self,x,valor):
        while x != None and valor != x.getDado():
            if valor < x.getDado():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        return x
    
    def inorder_Tree_Walk(self,x):
        if x != None:
            self.inorder_Tree_Walk(x.getFilhoEsquerdo())
            self.__print= self.__print + str(x.getDado())+ " "
            self.inorder_Tree_Walk(x.getFilhoDireito())
    def posorder_tree_walk(self,x):
        if x != None:
            self.posorder_tree_walk(x.getFilhoEsquerdo())
            self.posorder_tree_walk(x.getFilhoDireito())
            self.__print= self.__print + str(x.getDado())+ " "
    def preorder_tree_Walk(self,x):
        if x != None:
            self.__print= self.__print + str(x.getDado())+ " "
            self.preorder_tree_Walk(x.getFilhoEsquerdo())
            self.preorder_tree_Walk(x.getFilhoDireito())
            
    def recursive_tree_search(self,x,value):
        if x == None or value == x.getDado():
            return x        
        if value < x.getDado():
            return self.tree_search(x.getFilhoEsquerdo(), value)
        else:
            return self.tree_search(x.getFilhoDireito(), value)
        
    def Interative_tree_search(self,x,value):
        while x != None and value != x.getDado():
            if value < x.getDado():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        return x
            
    def tree_Minimum(self,nodo):
        while nodo.getFilhoEsquerdo() != None:
            nodo = nodo.getFilhoEsquerdo()
        return nodo
    
    def tree_Maximum(self,nodo):
        while nodo.getFilhoDireito() != None:
            nodo = nodo.getFilhoDireito()
        return nodo
    
    def tree_Sucessor(self,nodo):
        if nodo.getFilhoDireito()!= None:
            return self.tree_Minimum(nodo.getFilhoDireito())
        y = nodo.getPai()
        while y != None and nodo == y.getFilhoDireito():
            nodo = y
            y = y.getPai()
        return y
    
    def tree_Predecessor(self,nodo):
        if nodo.getFilhoEsquerdo()!= None:
            return self.tree_Maximum(nodo.getFilhoEsquerdo())
        y = nodo.getPai()
        while y != None and nodo == y.getFilhoEsquerdo():
            nodo = y
            y = y.getPai()
        return y
            
           
    def tree_insert(self,valor):
        nodo = TreeNode(valor)
        y = None
        x = self.getRaiz()
        while x != None:
            y = x
            if nodo.getDado() < x.getDado():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        nodo.setPai(y)
        if y == None:
            self.setRaiz(nodo)
        else:
            if nodo.getDado()< y.getDado():
                y.setFilhoEsquerdo(nodo)
            else:
                y.setFilhoDireito(nodo)
                
    
    def tree_delete(self,nodo):
        if nodo.getFilhoEsquerdo()== None or nodo.getFilhoDireito() == None:
            y = nodo
        else:
            y = self.tree_Sucessor(nodo)
        if y.getFilhoEsquerdo() != None:
            x = y.getFilhoEsquerdo()
        else:
            x = y.getFilhoDireito()
        if x != None:
            x.setPai(y.getPai())
        if y.getPai()==None:
            self.setRaiz(x)
        elif y == y.getPai().getFilhoEsquerdo():
            y.getPai().setFilhoEsquerdo(x)
        else:
            y.getPai().setFilhoDireito(x)
        if y != nodo:
            nodo.setDado(y.getDado())
        return y
    
    def transplant(self,u,v):
        if u.getPai() == None:
            self.setRaiz(v)
        elif u == u.getPai().getFilhoEsquerdo():
            u.getPai().setFilhoEsquerdo(v)
        else:
            u.getPai().setFilhoDireito(v)
        if v != None:
            v.setPai(u.getPai())
    def deletar(self,z):
        if z.getFilhoEsquerdo() == None:
            self.transplant(z, z.getFilhoDireito())
        elif z.getFilhoDireito() == None:
            self.transplant(z, z.getFilhoEsquerdo())
        else:
            y = self.tree_Minimum(z.getFilhoDireito())
            if y.getPai() != z:
                self.transplant(y, y.getFilhoDireito())
                y.setFilhoDireito(z.getFilhoDireito())
                y.getFilhoDireito().setPai(y)
            self.transplant(z, y)
            y.setFilhoEsquerdo(z.getFilhoEsquerdo())
            y.getFilhoEsquerdo().setPai(y)
                
                
                
                            
    def MaiorMenor(self,valor):
        nodo = self.__raiz
        self.__kappa= valor
        self.Inorder2(nodo)
        saida = self.__pre
        self.__pre = 0
        self.__kappa = 0
        return saida
    
    def Inorder2(self,nodo):
        if nodo!=None:
            self.Inorder2(nodo.getFilhoEsquerdo())
            if nodo.getDado()> self.__pre and nodo.getDado()<self.__kappa:
                self.__pre = nodo.getDado()
            self.Inorder2(nodo.getFilhoDireito())
            

cont = 0 
while True:
    try:                    
        entrada = int(input())
        cont+=1
        print("Caso %d:"%(cont))
        Arvore = BinaryTree()
        for i in range(entrada):
            entrada1 = input()    
            if entrada1 == "PRE":
                if Arvore.getRaiz() == None:
                    print(0)
                else:
                    Arvore.preorder_tree_Walk(Arvore.getRaiz())
                    print(Arvore.getprint()[:-1])
                    Arvore.resetprint()
            elif entrada1 == "IN":
                if Arvore.getRaiz() == None:
                    print(0)
                else:
                    Arvore.inorder_Tree_Walk(Arvore.getRaiz())
                    print(Arvore.getprint()[:-1])
                    Arvore.resetprint()
            elif entrada1 == "POST":
                if Arvore.getRaiz() == None:
                    print(0)
                else:
                    Arvore.posorder_tree_walk(Arvore.getRaiz())
                    print(Arvore.getprint()[:-1])
                    Arvore.resetprint()
            elif entrada1[0] == "A":
                Arvore.tree_insert(int(entrada1[2:]))
            elif entrada1[0] == "B":
                Nodo = Arvore.Interative_tree_search(Arvore.getRaiz(),int(entrada1[2:]))
                if Nodo == None:
                    print(0)
                else:
                    Arvore.deletar(Nodo)
            elif entrada1[0] == "C":
                x = Arvore.MaiorMenor(int(entrada1[2:]))
                print(x)
    except:
            break
        
        
                    