"""
Escribir una función empaquetar para una lista, donde epaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
, (1, 2), (3, 2)].
"""

def empaquetar(lista):
    if not lista:
        return []

    res = []
    elemento_actual = lista[0]
    cantidad = 0
    for elemento in lista:
        if elemento == elemento_actual:
            cantidad += 1
        else:
            tupla = (elemento_actual, cantidad)
            res.append(tupla)
            elemento_actual = elemento
            cantidad = 1

    tupla = (elemento_actual, cantidad)
    res.append(tupla)
    return res
print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]))
