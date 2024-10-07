def fibonacci_rec(n):
    #   Caso base. Cuando n vale 0 o 1.
    if (n <= 1):
        return (n)
    #   Recursividad
    else:
        return fibonacci(n-1) + fibonacci(n-2) #Tremendamente ineficiente para números grandes N^2

def fibonacci(n):
    if (n <= 1):
        return (n)
    ultimo, penultimo = 1, 0
    for _ in range(2, n + 1):
        penultimo, ultimo = ultimo, penultimo + ultimo
    
    return ultimo
     
# Llamada
n = int(input("Introduce un número para calcular su sucessión de Fibonacci\n "))
print(f"El término  n-ésimo de la sucesión de Fibonacci es: {fibonacci(n)}")
