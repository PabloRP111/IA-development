def del_dup(lista):
    b = 1
    new_list = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (lista[i] == lista[j]):
                b = 0
        if (b == 0):
            if (lista[i] not in new_list):
                new_list.append(lista[i])
        b = 1
    return new_list

lista = [2, 3, 2, 4, 5, 6, 3, 7, 7, 8]
new_list = del_dup(lista)
print(f"List -> {lista}\nNo dups List -> {new_list}\n")    