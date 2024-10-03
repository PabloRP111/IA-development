def mult(n:int, n2:int):
    m = 0
    neg = 0
    if ((n < 0 and n2 > 0) or (n2 < 0 and n > 0)):
        neg = 1
    if (neg == 0):
        for i in range(n):
            m += n2
    else:
        for i in range(abs(n)):
            m -= abs(n2)
    print(f"{n} * {n2} = {m}")

def div(n:int, n2:int):
    m = abs(n)
    neg = 0
    if (n2 > n):
        return (print(f"{n} * {n2} = 0"))
    if ((n < 0 and n2 > 0) or (n2 < 0 and n > 0)):
        neg = 1
    if (neg == 0):
        for i in range(2, n2):
            m -= n2
    else:
        m = - abs(n2)
        for i in range(1, abs(n2 -1)):
            m -= abs(n2)
    print(f"{n} / {n2} = {m}")

operation = 0
while (operation != 5):
    operation = int(input("Dime la operación que quieres realizar\n\t1.Suma\n\t2.Restar\n\t3.Multiplicar\n\t4.Dividir\n\t5.Salir\n"))
    if (operation < 1 or operation > 5):
        print("Operación Incorrecta")
    else:
        if (operation == 5):
            print("Exit")
        else:
            n = int(input("Dime el primer número\n"))
            n2 = int(input("Dime el segundo número\n"))
            if (operation == 1):
                print(f"{n} + {n2} = {n + n2}")
            elif (operation == 2):
                print(f"{n} - {n2} = {n - n2}")
            elif (operation == 3):
                mult(n, n2)
            elif (operation == 4):
                div(n, n2)