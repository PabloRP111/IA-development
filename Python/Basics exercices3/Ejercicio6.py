def binary_search(list1, element):
    pos = -1
    for i in range(0, int((len(list1)/2) + 1)):
        if (element == list1[i]):
            pos = i
        if (element == list1[int(-(i + 1))]):
            pos = len(list1) -(i + 1)
        if (pos != -1):
            return pos
    return pos

lista = [2, 3, 2, 4, 5, 6, 3, 7, 7, 8]
p = binary_search(lista, 7)
print(f"List -> {lista} posición {p}\n")  