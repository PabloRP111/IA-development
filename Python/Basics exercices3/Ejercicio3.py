import random

def is_dup(lista):
    c = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (lista[j] == lista[i]):
                return True
    return False

def generate_random(i):
    lista = []
    for _ in range(i):
        lista.append(random.randint(1, 100)) 
    return lista

i = 0
lista = generate_random(23)
print(f"List -> {lista}\nHay valores repetidos? {is_dup(lista)}\n")