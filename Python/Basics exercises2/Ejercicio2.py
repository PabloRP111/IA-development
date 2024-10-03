str = input("Dame un str\n")
c = input("Dame un caracter\n")
i = 0
n = 0

while (i < len(str)):
    if (str[i] == c):
        n += 1
    i += 1
print(f"{c} aparece {n} veces")