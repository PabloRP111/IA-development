año = int(input("Dime un año\n"))

if (año < 0):
    año *= -1
if (año % 4 != 0):
    print("El año no es bisiesto")
else:
    if (año % 100 == 0):
        if (año % 400 == 0):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")