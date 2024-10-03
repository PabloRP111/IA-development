str = input("Dame un cadena de caracteres\n")
reversed_str = ""
i = len(str)

while (i > 0):
    reversed_str = reversed_str + str[i - 1]
    i -= 1
print(f"El inverso de {str} es {reversed_str}")
