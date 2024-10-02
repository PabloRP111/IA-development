media = float(0)
n = float(0)
i = 0

while(n != -1):
    n = float(input("Dime un número positivo o -1 para parar el bucle\n"))
    if (n == -1):
        if (media == 0):
            media = -1
        break
    if (n <= -2):
        print("Dije que nada de negativos :/")
    else:
       i += 1
       media += n
print("La media aritmética es " + str(media / i))
