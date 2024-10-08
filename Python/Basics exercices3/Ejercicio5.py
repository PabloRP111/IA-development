def search(lista, searched):
    pos = -1
    for i in range(len(lista)):
        if (lista[i] == searched):
            pos = i
            return pos
    return pos

lista = [2, 3, 2, 4, 5, 6, 3, 7, 7, 8]
p = search(lista, 7)
print(f"List -> {lista} posición {p}\n")  