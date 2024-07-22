num = int(input("Digite um numero: "))
if num > 1:
    for i in range(2, num):
        if num%i==0:
            print(f'{num} Não e um numero primo')
            break
    else:
        print(f"{num} E numero Primo")        


