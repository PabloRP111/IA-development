def binary_search(lista, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if lista[mid] == x:
            return mid
        elif lista[mid] > x:
            return binary_search(lista, low, mid - 1, x)
        else:
            return binary_search(lista, mid + 1, high, x)
    else:
        return -1

lista = [1, 4, 6, 8, 13, 18]
n = int(input("Dime un número para buscar en la lista\n"))

if (binary_search(lista, 0, len(lista)-1, n) != -1):
    print(f"El número {n} esta en la lista")
else:
    print(f"El número {n} no esta en la lista")
