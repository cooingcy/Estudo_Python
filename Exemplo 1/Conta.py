class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    def saque(self, valor):
        if (self._saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self._saldo += valor
        print("Depósito realizado com sucesso")

    def extrato(self):
        print("Cliente:", self._titular, "Saldo Atual:", self._saldo)

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if (valor < 0):
            print("Saldo não pode ser negativo")
        else:
            self._saldo = valor

    @property
    def titular(self):
        return self._titular

    @property
    def numero(self):
        return self._numero
