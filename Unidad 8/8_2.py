def maximo(numeros):
    '''
    Devuelve el valor máximo de la lista de números
    '''
    if len(numeros) == 0:
        return None

    primer_numero = numeros[0]
    anterior = primer_numero
    for numero in numeros:
        if anterior < numero:
            anterior = numero
    return anterior

def maximo_y_posicion(numeros):
    '''
    Devuelve una tupla con el valor máximo de la lista de números y su posición
    '''
    if len(numeros) == 0:
        return (None, -1)

    max = maximo(numeros)
    posicion = 0
    for i in numeros:
        if i != max:
            posicion += 1
        else:
            break
    return (max, posicion)
print(maximo_y_posicion([3, 4, 2]))
