def multmatrix(matriz_a, matriz_b):
    if (matriz_a):
        filas_a = len(matriz_a)
        columnas_a = len(matriz_a[0])
    else:
        columnas_a = 0
    if (matriz_b):
        filas_b = len(matriz_b)
        columnas_b = len(matriz_b[0])
    else:
        columnas_b = 0    
    if columnas_a != filas_b:
        return "Las matrices no se pueden multiplicar: el número de columnas de A no coincide con el número de filas de B."
    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(filas_b):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return resultado

matriz_a = [[2, 9, 3], [1, 7, 7]]
matriz_b = [[2, 5], [8, 7], [3, 7]]

print(f"Resultado: {multmatrix(matriz_a, matriz_b)}")
