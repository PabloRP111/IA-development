clave_correcta = "eureka"
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    clave_ingresada = input("Introduce la clave: ")

    if clave_ingresada == clave_correcta:
        print("¡Clave correcta! Acceso concedido.")
        break
    else:
        intentos += 1
        print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")

if intentos == max_intentos:
    print("Has agotado tus 3 intentos. Acceso denegado.")
