'''

Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
d) Dicha cadena en sentido inverso. Ej.: 'holamundo!' debe imprimir '!odnumaloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.

'''

#a)
def imprimir_2_primeros_caracteres(cadena):
    print(cadena[0:2])

#b)
def imprimir_3_ultimos_caracteres(cadena):
    print(cadena[-3:])

#d)
def sentido_inverso(cadena):
    for i in range(len(cadena) - 1, -1, -1):
        print(cadena[i], end = '')

#e)
def normal_e_inversa(cadena):
    print(cadena, end = "")
    sentido_inverso(cadena)

#f)
def cada_dos_c(cadena):
    for c in range(0, len(cadena), 2):
        print(cadena[c], end = '')
