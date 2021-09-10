def validar_direccion():
    while True:
        direccion = input("Ingrese una dirección IPv4 válida : ")
        numeros = direccion.split(".")
        for numero in numeros:
            if 0 <= int(numero) <= 255:
                return ".".join(numeros)

print(validar_direccion())
