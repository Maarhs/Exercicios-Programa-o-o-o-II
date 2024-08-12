# 1. Escreva um código que receba o nome de uma pessoa e imprima uma
# saudação personalizada na tela com o nome do usuário.


def saudação(nome):
    nome = nome.capitalize()
    print(f"Seja muito bem vindo!! {nome}, é uma honra te-lo por aqui!")

saudação(input("Digite seu nome: "))