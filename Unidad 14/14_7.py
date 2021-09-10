'''
Escribir una función llamada tail que recibe un archivo y un número N e imprime
las últimas N líneas del archivo. Durante el transcurso de la función no puede
haber más de N líneas en memoria.
'''
from cola import Cola
def tail(ruta_archivo, n):
    ultimas_lineas = Cola()
    with open(ruta_archivo) as archivo:
        cantidad_lineas = 0
        for linea in archivo:
            ultimas_lineas.encolar(linea)
            cantidad_lineas += 1
            if cantidad_lineas > n:
                ultimas_lineas.desencolar()
    while not ultimas_lineas.esta_vacia():
        print(ultimas_lineas.desencolar())
