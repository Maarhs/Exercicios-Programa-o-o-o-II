# 3. Faça um programa que receba três números do usuário, e identifique o maior
# através de uma função e o menor número através de outra função.


def menor(n1,n2,n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    print(f"O menor numero é: {menor}")
    
def maior(n1,n2,n3):
    maior = n1
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    print(f"O maior numero é: {maior}")

lista = []

for i in range(1,4):
    num = int(input(f"Digite o {i}° numero: "))
    lista.append(num)

maior(lista[0],lista[1],lista[2])
menor(lista[0],lista[1],lista[2])






