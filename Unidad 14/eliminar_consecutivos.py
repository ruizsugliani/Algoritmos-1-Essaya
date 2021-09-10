"""
Escribir una funcion que reciba una pila de numeros y elimine de la misma los elementos
consecutivos que estan repetidos. Se pueden usar estructuras auxiliares. La funcion no devuelve
nada, simplemente modica los elementos de la pila que recibe por parametro.
Por ejemplo: remover duplicados consecutivos(Pila([2, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 7])) Genera: Pi-
la([2, 8, 3, 2, 3, 1, 7]).
"""
from pila import Pila
def remover_consecutivos(pila):
    temporal = Pila()
    while not pila.esta_vacia():
        numero = pila.desapilar()
        if temporal.esta_vacia():
            temporal.apilar(numero)
        if not temporal.estaba() and numero != temporal.ver_tope():
            temporal.apilar(numero)

    while not temporal.esta_vacia():
        numero = temporal.desapilar()
        pila.apilar(numero)
    return 
