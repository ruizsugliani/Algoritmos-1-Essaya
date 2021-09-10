"""
Escribir un programa que pida dos números enteros al usuario (a y b) e imprima
los primeros a múltiplos de b. El programa debe validar que cada número que
ingrese el usuario sea un entero positivo y, en caso de que no lo sea,
solicitarlo nuevamente (hasta que se ingrese algo correcto).
"""

#programa
#pide 2 enteros positivos al usuario (a y b)
#en caso de que no cumplan esto , solicitarlo nuevamente
#imprime los a multiplos de b

def main():
    a = int(input("Ingrese el numero a: "))
    b = int(input("Ingrese el numero b: "))
    while a < 0:
        a = int(input("Ingrese el numero a: "))
    while b < 0:
        b = int(input("Ingrese el numero b: "))
    for i in range(1, a + 1):
        print(i*b)


"""
Escribir una función que recibe una lista de cadenas y un número n y devuelve
una nueva lista de cadenas donde cada cadena tiene longitud n (con una
posible subcadena final de longitud menor a n) con el contenido de la
lista de cadenas recibida.
"""
def subcadenas(lista, n):
    res = []
    cadena_unificada = "".join(lista)
    actual = ""
    for c in cadena_unificada:
        actual += c
        if len(actual) % n == 0:
            res.append(actual)
            actual = ""
    if actual:
        res.append(actual)            
    return res

print(subcadenas(["algoritmos", "es", "lo", "mas"], 3))
"""
Escribir una funcion que sacuda una matriz. Es decir, que las filas pares,
las rote un elemento hacia la derecha, y las filas impares, hacia la izquierda.
Esta función debe trabajar sobre la matriz recibida, no debe devolver una nueva.
La matriz esta representada como una lista de listas donde cada sublista es una
fila de la matriz.
"""

#funcion
#rota las filas pares un elemento hacia la derecha
#rota las filas impares un elemento hacia la izquierda

def sacudir_matriz(lista):
    for i in range(len(lista)):
        if i % 2 != 0:
            i.pop()
            i.append(lista1[0])
            i.insert(0, lista1[-1])
        else:
            if i % 2 == 0:
                i.pop()
                i.insert(lista[-2], lista[-1])
                i.insert(lista[-1], lista[0])
    return lista

def sacudir_matriz(matriz):
    for i, fila in enumerat(matriz):
        if i % 2 == 0:
            matriz[i] = fila [-1] + fila[:-1]
        else:
            matriz[i] = fila [1:] + fila[0]
