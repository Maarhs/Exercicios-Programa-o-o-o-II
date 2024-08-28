'''Suponha que você está desenvolvendo um sistema de biblioteca. Crie a classe Livro com as seguintes características:
- Atributos: titulo, autor, ano_publicacao.
- Métodos: exibir_detalhes.'''

class Livro:
    def __init__(self):
        self.titulo = "O Pequeno Princípe"
        self.autor = "Antoine de Saint-Exupépy"
        self.ano_publicacao = 1943
    def exibir_detalhes(self):
        return self.titulo, self.autor, self.ano_publicacao
liv1= Livro()
print(liv1.exibir_detalhes())





