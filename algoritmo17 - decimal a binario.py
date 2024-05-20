numero = int(input("Ingrese número: "))
residuos = []
cociente = numero
while cociente > 1:
    residuo = cociente % 2
    residuos.append(residuo)
    cociente = cociente//2
residuos.append(cociente)
residuos.reverse()
if len(residuos) % 4 !=0:
    ceros = 4 - len(residuos) % 4
    print(ceros)
    i = 0
    while i < ceros:
        i = i + 1
        residuos.insert(0,0)
print(residuos)
i = 0
for digito in residuos:
 if i == 4:
    print("", end="")
    i = 0
    i = i + 1
    print(digito, end="")