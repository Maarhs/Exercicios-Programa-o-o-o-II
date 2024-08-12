# 6. Faça um programa que converta da notação de 24 horas para a notação de 12
# horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
# dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
# conversão e uma para personalizar a saída.


def notacao(horas):
    if 12 < horas < 24:
        hora_c = horas-12
        print(f"{hora_c}:{min}")
    elif 0 < horas < 13:
        hora_c = horas
        print(f"{hora_c}:{min}")
    else:
        print("erro!")

hora = input("Digite as horas: ")
horas = int(hora[:2])
min = int(hora[3:])
notacao(horas)