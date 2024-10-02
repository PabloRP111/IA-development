n = int(input("Dime el tamaño de tu escalera\n"))

for i in range(n):
    for aux in range(n - i):
        print("*", end="")
    print()