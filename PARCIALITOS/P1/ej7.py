"""
Escribir una funcion que dada una matriz representada como una lista de listas
de numeros (donde cada sublista representa unala), devuelva una lista con los
maximos de cada columna. Ejemplo:
maximos_columnas([
                [1, 2, 8, 4],
                [6, 7, 3, 3], -> [6, 7, 8, 9]
                [6, 5, 4, 9]])
"""
#crear lista de maximos
#recorrec cada columno
#calcular el maximo de dicha maximos_columnas
#agregar el maximo a la lista
#devolver maximos

def maximos_columnas(matriz):
    maximos = []
    for c in range(len(matriz[0])):
        maximo = matriz[0][c]
        for f in range(len(matriz)):
            if matriz[f][c] > maximo:
                maximo = matriz[f][c]
        maximos.append(maximo)
    return maximos

print(maximos_columnas(([[1, 2, 8, 4],[6, 7, 3, 3],[6, 5, 4, 9]])))
