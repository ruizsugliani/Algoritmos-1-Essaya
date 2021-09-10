import random

# La siguiente línea de código hace que random.randrange siempre genere la misma
#secuencia de números.
# Es necesaria para que cada vez que se corran las pruebas se obtengan los mismos
#resultados. En un programa "real" no debería estar.
random.seed(37)

def main():
    numero = int(input("Ingrese un número: "))


main()
