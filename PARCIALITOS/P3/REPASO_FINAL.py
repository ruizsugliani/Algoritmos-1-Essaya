'''
147)Escribir una función que reciba por parámetro dos pilas y modifique su contenido
de manera que los elementos de la primer pila queden en la segunda, y los de la
segunda en la primera manteniendo el orden original de los elementos.
Como estructuras auxiliares, se pueden utilizar únicamente pilas y/o colas.
'''
from pila import Pila

def intercambiar(pila1, pila2):
    aux1 = Pila()
    aux2 = Pila()
    while not pila1.esta_vacia() and not pila2.esta_vacia():
        if not pila1.esta_vacia():
            aux1.apilar(pila1.desapilar())

        if not pila2.esta_vacia():
            aux2.apilar(pila2.desapilar())

    while not aux1.esta_vacia() and not aux2.esta_vacia():
        pila1.apilar(aux2.desapilar())
        pila2.apilar(aux1.desapilar())

    return

'''
148)Escribir una función que reciba una pila de números y elimine de la misma los
elementos consecutivos que estén repetidos. La función debe actuar in place
sobre la pila que recibe por parámetro. Por ejemplo:

remover_duplicados_consecutivos(Pila([2, 5, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 8, 7]))
    → Pila([2, 5, 8, 3, 2, 3, 1, 8, 7])
'''
from pila import Pila

def remover_duplicados_consecutivos(pila):
    auxiliar = Pila()
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if auxiliar.esta_vacia():
            auxiliar.apilar(elemento)
        elif not auxiliar.esta_vacia() and elemento != auxiliar.ver_tope():
            auxiliar.apilar(elemento)

    while not auxiliar.esta_vacia():
        pila.apilar(auxiliar.desapilar())

    return
"""
149)Escribir una función intercalar(pilas) que reciba una secuencia de pilas y
devuelva una pila con los elementos de todas las pilas intercalados, manteniendo
el orden relativo. Las pilas originales deben quedar vacías.
Ejemplo:
intercalar([Pila(1, 2), Pila(3, 4, 5, 6), Pila(7)])
   → Pila(1, 3, 7, 2, 4, 5, 6)
"""
from pila import Pila

def intercalar(pilas):
    aux = Pila()
    res = Pila()
    for i in range(len(pilas)):
        while not pilas[i].esta_vacia():
            for pila in pilas:
                if not pila.esta_vacia():
                    aux.apilar(pila.desapilar())

    while not aux.esta_vacia():
        res.apilar(aux.desapilar())

    return res

"""
150)Escribir una funcion transferir(p1, p2) que recibe dos pilas y transfiere todos los elementos de p1
al tope de p2, de forma tal que queden en el mismo orden (es decir, el elemento que estaba inicialmente
en el tope de p1 debe quedar en el tope de p2). La pila p1 debe quedar vacía al finalizar la función.
"""
from pila import Pila

def transferir(p1, p2):
    aux = Pila()
    while not p1.esta_vacia():
        aux.apilar(p1.desapilar())

    while not aux.esta_vacia():
        p2.apilar(aux.desapilar())

"""
154)Implementar una función que reciba una pila de números enteros ordenados ascendentemente y determine
si todos los números son consecutivos. La pila debe preservar su estado inicial. Ejemplo:

consecutivos(Pila(1,2,3,4,5,6)) → True
consecutivos(Pila(1,2,4,5,6,7)) → False # 2 y 4 no son consecutivos
"""


"""
155)Implementar una función que, dada una pila de números, devuelva otra pila que contenga únicamente los
números pares de ésta (manteniendo el orden relativo de los elementos según como estaban en la original).
La pila original debe preservar su estado original al salir de la función. Es decir, debe conservar
todos los elementos que tenía y el orden de los mismos antes de que la función fuese invocada.
"""
from pila import Pila

def son_pares(pila):
    temporal = Pila()
    auxiliar = Pila()
    pares = Pila()
    while not pila.esta_vacia():
        numero = pila.desapilar()
        auxiliar.apilar(numero)
        if numero % 2 == 0:
            temporal.apilar(numero)

    while not temporal.esta_vacia():
        pares.apilar(temporal.desapilar())
    while not auxiliar.esta_vacia():
        pila.apilar(auxiliar.desapilar())

    return pares

"""
156)Dada una pila de enteros, escribir una función que determine si es piramidal.
Una pila de enteros es piramidal si cada elemento es menor a su elemento inferior
(el elemento inferior es el siguiente en el sentido hacia la base de la pila).
Al finalizar la ejecución, la pila debe quedar en el mismo estado con el que empezó.
"""

'''
162)Se tiene una cola de gente en el Parque de la Costa y el dueño, en honor al
cumpleaños de su tía Marta decide reacomodar la cola y priorizarle el lugar
a las personas cuyo nombre comienza con M. Para ello hay que realizar una
función que reciba una cola con nombres y reubique aquellos nombres que
comienzan con M dejándolos primeros, siempre respetando el orden de llegada
relativo entre aquellos que tengan la misma condición (entre las personas que
empiezan con M por un lado, y entre los que no por otro).
'''
from cola import Cola

def prioridades(cola):
    comunes = Cola()
    prioritarios = Cola()
    while not cola.esta_vacia():
        nombre = cola.desencolar()
        if nombre[0] == "M":
            prioritarios.encolar(nombre)
        else:
            comunes.encolar(nombre)

    while not prioritarios.esta_vacia():
        cola.encolar(prioritarios.desencolar())

    while not comunes.esta_vacia():
        cola.encolar(comunes.desencolar())

    return cola

"""
165)Implementar una función que reciba una cola y un elemento y modifique la cola original
eliminando todas las apariciones del elemento recibido por parámetro. El resto de los
elementos deben preservar el orden original en el que estaban
"""
from cola import Cola

def eliminar_apariciones(cola, elemento):
    auxiliar = Cola()
    while not cola.esta_vacia():
        elem = cola.desencolar()
        if elem != elemento:
            auxiliar.encolar(elem)

    while not auxiliar.esta_vacia():
        cola.encolar(auxiliar.desencolar())
    return cola
