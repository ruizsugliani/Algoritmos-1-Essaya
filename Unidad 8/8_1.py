#a)
def contar_apariciones(lista,elemento):
    '''
    Recibe una lista desordenada y un elemento, y devuelve la cantidad de veces
    que el elemento aparece en la lista.
    '''
    contador = 0
    for elem in lista:
        if elem == elemento:
            contador += 1
    return contador

#b)
def buscar_primera_aparicion(lista, elemento):
    '''
    Escribir una función que reciba una lista desordenada y un elemento,
    que busque la primera coincidencia del elemento en la lista y devuelva
    su posición.
    '''
    if elemento in lista:
        return lista.index(elemento)
    return -1

#c)
def buscar_apariciones(lista, elemento):
    '''
    Dada una lista desordenada y un elemento, busca todos los elementos
    que coincidan con el pasado por parámetro y devuelve una lista con las
    posiciones.
    '''
    res = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            res.append(i)
    return res
