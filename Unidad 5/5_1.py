"""
Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando
a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.
"""

def main():
    hay_mas_notas = "s"
    notas = 0
    cantidad_de_notas = 0
    while hay_mas_notas == "s":
        nota = float(input("Ingresar nota: "))
        notas += nota
        cantidad_de_notas += 1
        hay_mas_notas = input("Desea agregar mas notas? <s/n> :")
    print(notas // cantidad_de_notas)

main()
