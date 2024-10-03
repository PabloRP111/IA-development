str = input("Dime un str\n")
i = 0
n_w = 1

while (i < len(str)):
    if (str[i] == ' '):
       n_w += 1
    i += 1
print(f"Hay {n_w} palabras")