while True:
    nome = input("digite seu nome: ")
    senha = input("digite sua senha: ")
    if nome != senha:
        print("Nome e senha valido")
        break
    else:
        print("Nome e senha Não podem ser Iguais!!")