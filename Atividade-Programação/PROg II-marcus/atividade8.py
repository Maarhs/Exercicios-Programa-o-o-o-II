p1 = input("Voce e idoso?(S/N): ").lower()
p2 = input("Voce e gestante?(S/N): ").lower()
p3 = input("vc e PCD?(S/N): ").lower()
perg = [p1,p2,p3]
s =[]
for perg in (perg):
     if perg=="s":
        s.append(perg)
     break
if len(s) > 0:
    print("Vc tem acesso a fila prioridade")
else:
    print("Vc Não tem acesso a fila prioridade")
