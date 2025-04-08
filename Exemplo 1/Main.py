# Classe public tem o "_" na frente, 
# Classe privada tem "__" (duplo) na frente,
# Classe protec tem "_" antes

class Main:
    pass

print("Testando o Objeto")

from Cliente import Cliente
from Conta import Conta

# Testando a class Cliente
c1 = Cliente("Lucas", "123456-7890")
print(c1)
print(c1.get_nome(), "e", c1.get_telefone())

# Testando a class Conta
conta = Conta(c1.get_nome(), 123456, 1000.00)
print(conta.titular, "Número: ", conta.numero, "Saldo: ", conta.saldo)

conta.deposito(100)
conta.saque(50)
conta.extrato()