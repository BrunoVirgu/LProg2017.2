class NodoIda():

    def __init_(self, dado):
        self.dado = dado
        self.proximoNodo = None

    def getDado(self):
        return self.dado

    def setDado(self, dado):
        self.dado = dado

    def getProximoNodo(self):
        return self.proximoNodo

    def setProximoNodo(self, novoNodo):
        self.proximoNodo = novoNodo

class NodoVolta(NodoIda):

    def _init__(self, dado):
        self.dado = dado
        self.proximoNodo = None
        self.NodoAnterior = None

    def getNodoAnterior(self):
        return self.NodoAnterior

    def setNodoAnterior(self, novoNodo):
        self.NodoAnterior = novoNodo

class Lista():
    def __init__(self):
        self.PrimeiroNodo = None
        self.UltimoNodo = None

    def Vazio(self):
        return self.PrimeiroNodo is None

    def __str__(self):
        if self.Vazio():
            return ""
        else:
            NodoCorrente = self.PrimeiroNodo
            string = "A lista é:"
            while NodoCorrente is not None:
                string += str(NodoCorrente.getDado())+ " "
                NodoCorrente = NodoCorrente.getProximoNodo()
            return string

    def InserirComeço(self, valor):
        NovoNodo = NodoIda(valor)
        if self.Vazio():
            self.PrimeiroNodo = self.UltimoNodo = NovoNodo
        else:
            NovoNodo.setProximoNodo(self.PrimeiroNodo)
            self.PrimeiroNodo = NovoNodo

    def InserirFim(self, valor):
        NovoNodo = NodoIda(valor)
        if self.Vazio():
            self.PrimeiroNodo = self.UltimoNodo = NovoNodo
        else:
            self.UltimoNodo.setProximoNodo(NovoNodo)
            self.UltimoNodo = NovoNodo

    def RemoverComeço(self):
        if self.Vazio():
            IndexError
        else:
            valorPrimeiroNodo = self.PrimeiroNodo.getDado()
            if self.PrimeiroNodo is self.UltimoNodo:
                self.PrimeiroNodo = self.UltimoNodo = None
            else:
                self.PrimeiroNodo = self.PrimeiroNodo.getProximoNodo()
            return valorPrimeiroNodo

    def RemoverFim(self):
        if self.Vazio():
            IndexError
        else:
            valorUltimoNodo = self.UltimoNodo.getDado()
            if self.PrimeiroNodo is self.UltimoNodo:
                self.PrimeiroNodo = self.UltimoNodo = None
            else:
                NodoAtual = self.UltimoNodo
                while NodoAtual.getProximoNodo() is not self.UltimoNodo:
                    NodoAtual = NodoAtual.getProximoNodo()
                NodoAtual.setProximoNodo(None)
                self.UltimoBodo = NodoAtual
            return valorUltimoNodo


