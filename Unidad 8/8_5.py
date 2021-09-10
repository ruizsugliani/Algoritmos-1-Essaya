def busqueda_binaria(lista, elemento):
    '''
    Recibe una lista ordenada y un elemento. Si el elemento se encuentra en la lista,
    debe encontrar su posición mediante búsqueda binaria y devolverlo. Si no se encuentra,
    debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
    '''
    if elemento not in lista:
        buscar_y_agregar(lista, elemento)

    if elemento in lista:
        izq = 0
        der = len(lista) - 1

        while izq <= der:
            medio = (izq + der) // 2

            if lista[medio] == elemento:
                return medio

            if lista[medio] > elemento:
                der = medio - 1

            else:
                izq = medio + 1

def buscar_y_agregar(lista, elem):
    izq = 0
    der = len(lista) - 1

    while der > izq:
        medio = (der+izq)//2
        if lista[medio] == elem:
            return medio
        if lista[medio] > elem:
            der = medio - 1
        else:
            izq = medio + 1

    if lista[medio] < elem:
        lista.insert(medio + 1, elem)
        return medio + 1

    lista.insert(medio, elem)

    return medio
print(busqueda_binaria([1, 2, 4, 7, 12, 45], 25))
