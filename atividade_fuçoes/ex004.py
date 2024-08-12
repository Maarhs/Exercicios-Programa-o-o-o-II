# 4. Crie um programa de câmbio. Nesse programa adicione funções que
# realizem conversões de real para dólar, real para euro e real para peso
# argentino, conforme o nome do país fornecido pelo usuário. Utilize os valores:
# 1,00 real = 0,18 dólar para Estados Unidos;
# 1,00 real = 0,16 euro para Portugal;
# 1,00 real = 0,0061 peso para Argentina;

def real_dolar(real):
    dolar = 0.18
    resul = real * dolar
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

def real_euro(real):
    euro = 0.16
    resul = real * euro
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

def real_peso_arg(real):
    peso_arg = 0.0061
    resul = real * peso_arg
    print(f"R$ {real} são equivalentes a $ {resul:.2f}")

real = float(input("Digite o valor em R$: "))
real_dolar(real)
real_euro(real)
real_peso_arg(real)