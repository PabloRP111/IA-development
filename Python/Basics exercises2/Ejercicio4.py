str = input("Dime un str\n")
new_str = ""

for i in range(len(str)):
    if str[i].isalpha():
        if str[i].islower():
            new_str = new_str + str[i].upper()
        else:
            new_str = new_str + str[i].lower()
    else:
        new_str = new_str + str[i]
print(f"El nuevo str es {new_str}")