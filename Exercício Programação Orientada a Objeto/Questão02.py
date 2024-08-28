'''Crie um sistema para aplicativo bancário, que possui a Classe ContaBancaria com as seguintes características:
- Atributos: titular, saldo, numero_conta e tipo_conta.
- Métodos: depositar, sacar, transferir e verificar_saldo.'''

class ContaBancaria:
    def __init__ (self):
        self.titular = "Luana"
        self.saldo = 1300
        self.numero_conta = 766576
        self.tipo_conta = "Poupança"
    def depositar(self, valor):
            self.saldo += valor
            return self.saldo
    def sacar(self, valor):
            if self.saldo >= valor:
                self.saldo -= valor
                return self.saldo
            else:
                print("Saldo insuficiente")
    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            return self.saldo, conta_destino.saldo
        else:
            print("Saldo insuficiente")
    def verificar_saldo(self):
        return self.saldo
                
conta1 = ContaBancaria()
conta2= ContaBancaria()
print(conta1.depositar(500))
print(conta1.sacar(200))
print(conta1.transferir(100, conta2))
print(conta1.verificar_saldo())