def esta_ordenada(self):
    actual = self.prim
    if not actual.prox:
        return True
    else:
        if actual.dato <= actual.prox.dato:
            self.prim = actual.prox
            return self.esta_ordenada()
        else:
            return False
def contar_elementos(pila):
    '''
    Funcion auxiliar la cual cuenta la cantidad de elementos de una pila y los devuelve,
    dejando la pila tal cual la recibio.
    '''
    c = 0
    temp = Pila()
    while not pila.esta_vacia():
        temp.apilar(pila.desapilar())
        c += 1
    while not temp.esta_vacia():
        pila.apilar(temp.desapilar())
    return c


def dividir_pila(pila, n):
    '''
    Funcion que recibe por parametro una pila y un numero n, devuelve una lista de pilas con n elementos
    preservando el orden de los elementos en la pila original.
    '''
    elementos_por_pila = contarelementos(pila) // n + 1
    pilas = [Pila() for  in range(elementos_por_pila)]
    i = 0
    cantidad_apilada = 0
    while not pila.esta_vacia():
        pilas[i % len(pilas)].apilar(pila.desapilar())
        cantidad_apilada += 1
        if cantidad_apilada % n == 0:
            i +=1

    for i in range(len(pilas)):
        final = Pila()
        while not pilas[i].esta_vacia():
            final.apilar(pilas[i].desapilar())
        pilas[i] = final

    return pilas
