n = int(input("Dime un número\n"))
sum_par = 0

for i in range(n):
    print(i , end=", ")
    if (i % 2 == 0):
        sum_par += i
print(str(n))
if (i % 2 == 0):
    sum_par += i
print("La suma de los números pares es " + str(sum_par))