n = int(input("Dime un número para saber su factorial\n"))

if n == 0:
	print("El factorial es 1")
else:
	aux = 1
	for i in range(n):
		aux *= (n - i)
	print(f"El factorial es {aux}")