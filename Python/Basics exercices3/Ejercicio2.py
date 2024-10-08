def alinacci(lista):
    new_list = lista.copy()
    for i in range(1, len(lista)):
        new_list[i] = new_list[i] + new_list[i - 1]
    return new_list

i = 0
lista = []
while (i >= 0):
    i = int(input("Dime un número para el array, -negativos para parar\n"))
    if (i >= 0):
        lista.append(i)
new_list = alinacci(lista)
print(f"List -> {lista}\nNew list -> {new_list}")
