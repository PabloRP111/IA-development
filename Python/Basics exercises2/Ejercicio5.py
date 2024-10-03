str = input("Dime un str \n")
substr = input("Dime un substr \n")

if (str.find(substr) >= 0):
    print(f"{str} contiene {substr}")
else:
    print(f"{str} no contiene {substr}")