def multmatrix(matriz_a, matriz_b):
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0]) if matriz_a else 0
    filas_b = len(matriz_b)
    columnas_b = len(matriz_b[0]) if matriz_b else 0
    
    if columnas_a != filas_b:
        return "Las matrices no se pueden multiplicar: el número de columnas de A no coincide con el número de filas de B."
    
    # Inicializar la matriz resultado con ceros
    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]
    
    # Multiplicar las matrices
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return resultado

matriz_a = [[2, 9, 3], [1, 7, 7]]
matriz_b = [[2, 5], [8, 7], [3, 7]]

print(f"La multiplicón es: {multmatrix(matriz_a, matriz_b)}")
