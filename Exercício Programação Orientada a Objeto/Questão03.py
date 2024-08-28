'''Desenvolva um sitema de estoque que possui a Classe produtos com as seguintes características:
Atributos: nome, preco, quantidade e codigo.
Métodos: calcular_total, atualizar_preco e verificar disponibilidade.'''

class Produtos():
    def __init__(self):
        self.nome = "Sorvete"
        self.preco = 2.80
        self.quantidade = 50
        self.codigo = 345455
    def calcular_total(self):
        return self.preco * self.quantidade
    def atualizar_preco(self):
        self.novo_preco = 3.00
        return self.novo_preco
    def verificar_disponibilidade(self):
        if self.quantidade > 0:
            return True
        else:
            return False
        
veri1 = Produtos()
print(veri1.calcular_total())
print(veri1.atualizar_preco())
print(veri1.verificar_disponibilidade())
