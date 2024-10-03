str = input("Dime un str\n")
substr = input("Dime un substr por el que empiece str\n")
i = 0

if (str < substr):
    print("Tu substr no aparece al principio de str")
else:
    while i < len(substr):
        if (substr[i] != str[i]):
            print("Tu substr no aparece al principio de str")
            break
        i += 1
    print("Tu substr aparece al principio de str")