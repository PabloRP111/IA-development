def diagsum(matriz):
    sum = 0
    for i in range(len(matriz)):
            sum += matriz[i][i]
    return (sum)

matriz = [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
print(f"la suma de la diagonal es {diagsum(matriz)}\n")
