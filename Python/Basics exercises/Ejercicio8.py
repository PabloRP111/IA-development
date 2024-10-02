n = int(input("Dime un número \n"))

if n <= 1:
    print("No es un número primo")
else:
    es_primo = True 

    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es un número primo")
    else:
        print("No es un número primo")