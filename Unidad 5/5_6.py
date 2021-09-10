"""
a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
y devuelva True si el número es una potencia de 2, y False en caso contrario.
b) Escribir una función que, dados dos números naturales pasados como parámetros,
devuelva la suma de todas las potencias de 2 que hay en el rango formado por
esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
es_potencia_de_dos, descripta en el punto anterior.
"""

#a)
def es_potencia_de_dos(n):
    '''
    Recibe como parametro un numero natural, devuelve True si es potencia de 2, y
    False en caso contrario.
    '''
    i = 1
    while True:
        potencia = 2 ** i
        if potencia < n:
            i += 1
            continue
        elif potencia == n:
            return True
        else:
            return False

def suma_potencias_de_dos(n,m):
    '''
    Dados dos numeros naturales como parametros, devuelve la suma de todas las
    potencias de 2 que hay en el rango formado por esos numeros.
    '''
    suma = 0
    for j in range(n, m):
        if es_potencia_de_dos(j):
            suma += j
        continue
    return suma
