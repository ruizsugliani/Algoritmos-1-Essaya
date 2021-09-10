"""
Escribir un programa que le pida al usuario que ingrese un número entero
positivo n y una cadena, e imprima la misma cadena pero con
un guión (-) cada n lugares.
"""
#programa
#pide al usuario que ingrese un numero positivo n y una cadena
#imprime la cadena con un guión cada n lugares
def main():
    n = int(input("Ingrese un numero positivo n : "))
    cadena = str(input("Ingrese una cadena : "))
    for c in range(0, len(cadena) - 1, n):
        cadena.split("-")
        print(cadena)
main()
