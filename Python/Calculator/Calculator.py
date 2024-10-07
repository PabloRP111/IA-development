#Función de multiplicar, la multiplicación se puede entender como la suma del valor absoluto de n, n2 veces o viceversa.
def mult(n:int, n2:int):
    m = 0
    neg = 0
    #Si el signo es distinto el resultado será negativo
    if ((n < 0 and n2 > 0) or (n2 < 0 and n > 0)):
        neg = 1
    #Esta es una manera diferente de hacerlo por la que he optado para variar de la función de división, en lugar de guardar el signo y multiplicarlo al final,
    #como hago en la función de abajo, decidi que cuando el signo sea negativo restare en lugar de sumar y viceversa, en el fondo la lógica es la misma
    if (neg == 0):
        for i in range(abs(n)):
            m += abs(n2)
    else:
        for i in range(abs(n)):
            m -= abs(n2)
    print(f"{n} * {n2} = {m}")

#Función de dividir, la división se puede entender como una la resta de n2 sobre n mientras abs(n) >= abs(n2)
def div(n:int, n2:int):
    neg = 1
    i = 0
    m = abs(n)
    if ((n < 0 and n2 > 0) or (n2 < 0 and n > 0)):
        neg = -1
    while (m >= abs(n2)):
        m -= abs(n2)
        i += 1
    #Multiplicamos por -1 si es negativo
    if (neg != 1):
        i *= -1
    print(f"{n} / {n2} = {i}")

operation = 0
#Bucle del programa
while (operation != 5):
    operation = int(input("Dime la operación que quieres realizar\n\t1.Suma\n\t2.Restar\n\t3.Multiplicar\n\t4.Dividir\n\t5.Salir\n"))
    #Comprobación de argumentos
    if (operation < 1 or operation > 5):
        print("Operación Incorrecta")
    else:
        #Salir del bucle y terminar programa
        if (operation == 5):
            print("Exit")
        else:
            n = int(input("Dime el primer número\n"))
            n2 = int(input("Dime el segundo número\n"))
            #Me niego a explicar las suma y la resta :)
            if (operation == 1):
                print(f"{n} + {n2} = {n + n2}")
            elif (operation == 2):
                print(f"{n} - {n2} = {n - n2}")
            elif (operation == 3):
                mult(n, n2)
            elif (operation == 4):
                div(n, n2)