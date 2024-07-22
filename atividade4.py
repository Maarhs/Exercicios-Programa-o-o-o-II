data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = map(int,data.split('/'))
if dia < 1 or dia > 31:
    print("dia invalido.")
else:
    if mes < 1 or mes > 12:
        print("mês invalido.")
    else:
        if ano <= 2024:
            print("ano invalido.")
        else:
            print("Data Valida.")
    
      