def obtener_minimo(listas):
    minimo = min(listas[0])
    for i in range(1, len(listas)):
        if listas[i][0] < minimo:
            minimo = listas[i][0]
        else:
            continue

    return minimo

def multi_merge(listas):
    resultado = []
    while listas:
        if [] in listas:
            listas.remove([])
            continue

        minimo = obtener_minimo(listas)

        for lista in listas:
            if minimo in lista:
                lista.remove(minimo)
                break
        resultado.append(minimo)
    return resultado


print(multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8]]))
print(multi_merge([[2, 4, 6, 8], [1, 3, 5, 7, 9]]))
print(multi_merge([[2, 4, 6, 8], [1, 3], [0], [4, 5, 6]]))

def pruebas():
    assert multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert multi_merge([[2, 4, 6, 8], [1, 3, 5, 7, 9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert multi_merge([[2, 4, 6, 8], [1, 3], [0], [4, 5, 6]]) == [0, 1, 2, 3, 4, 4, 5, 6, 6, 8]

    # OPCIONAL: agregar más casos de prueba. Sugerencias: probar distintos valores de k,
    # y listas de diferentes longitudes (no tienen por qué ser todas de la misma longitud).

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
