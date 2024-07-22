p1 = input("Telefonou para a vítima?(S/N): ").lower()
p2 = input("Esteve no local do crime?(S/N): ").lower()
p3 = input("Mora perto da vítima?(S/N): ").lower()
p4 = input("Devia para a vítima?(S/N): ").lower()
p5 = input("Já trabalhou com a vítima?(S/N)").lower()
policia = [p1,p2,p3,p4,p5]
s = []
for policia in policia:
    if policia == "s":
        s.append(policia) 
        if len(policia) == 5:
         print("Assassino")
         break
        if len(policia) > 3 or len(policia) < 4:
                print("Cúmplice")
                break
        if len(policia) < 2:
                print("Suspeita")
                break
        

