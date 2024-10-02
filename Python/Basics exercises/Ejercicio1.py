numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

if numero1 <= numero2 and numero1 <= numero3:
    if numero2 <= numero3:
        ordenados = [numero1, numero2, numero3]
    else:
        ordenados = [numero1, numero3, numero2]
elif numero2 <= numero1 and numero2 <= numero3:
    if numero1 <= numero3:
        ordenados = [numero2, numero1, numero3]
    else:
        ordenados = [numero2, numero3, numero1]
else:
    if numero1 <= numero2:
        ordenados = [numero3, numero1, numero2]
    else:
        ordenados = [numero3, numero2, numero1]

print("Los números ordenados son:", ordenados)
