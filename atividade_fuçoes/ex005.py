# 5. Escreva um programa que possa cadastrar clientes ou funcionários para uma
# loja. Se o usuário quiser cadastrar um cliente, dados de nome, endereço,
# CPF devem ser solicitados. Caso o usuário prefira adicionar um novo
# funcionário, dados de nome, salário, cargo e CPF devem ser requisitados.
# Utilize comandos de manipulação de string para personalizar a saída.

def cliente():
    dados = []
    dados.append(input("Digite o nome do cliente: "))
    dados.append(input("Digite o cpf do cliente: "))
    dados.append(input("Digite o endereco do cliente: "))
    print(f"Os dados do cliente são:\nNome: {dados[0]}, CPF: {dados[1]}, endereço: {dados[2]}")

def funci():
    dados = []
    dados.append(input("Digite o nome do funcionário: "))
    dados.append(input("Digite o cpf do funcionário: "))
    dados.append(input("Digite o endereco do funcionário: "))
    print(f"Os dados do funcionário são:\nNome: {dados[0]}, CPF: {dados[1]}, endereço: {dados[2]}")

tipo = input("Deseja cadastrar um C - Cliente ou F - Funcionário: ").upper()

if tipo == "C":
    cliente()
elif tipo == "F":
    funci()
else:
    print("EROO!")