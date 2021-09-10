from lista_enlazada import ListaEnlazada
from lista_enlazada import _Nodo
#126
'''
Se cuenta con una implementación de ListaEnlazada con únicamente una referencia al primer nodo. Se pide implementar un método unir_medio, que dada una segunda lista enlazada,
la inserte en el medio de la original.
Ejemplo: para las listas a→b→c→d y e→f→g, el resultado debe ser a→b→e→f→g→c→d.
No se puede recorrer ninguna lista más de una vez. Al finalizar la ejecución, la segunda lista debe quedar vacía.
'''
#127
'''
Implementar el método reduce dada una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Este método debe recibir una función y devolver el resultado de dicha reducción a la ListaEnlazada. Ejemplos:

    Para [1,2,3] y la función sumar debe devolver 6, ya que (1+2) + 3 = 6
    Para [1,2,3] y la función restar debe devolver -4, ya que (1-2) - 3 = -4
    Para [1] y la función restar debe devolver 1
    Para [] y la función sumar debe lanzar una excepción
'''


def reduce(self, f):
    if self.prim is None:
        raise Exception("Lista vacía.")

    else:
        actual = self.prim
        if not actual.prox:
            return actual.dato

        else:
            res = actual.dato
            while actual.prox:
                res = f(res, actual.prox.dato)
                actual = actual.prox
    return res


#128
'''
Implementar un método de la clase ListaEnlazada que elimine sobre la misma lista los elementos consecutivos repetidos.
La misma está implementada con únicamente una referencia al primer nodo.

L: [3 4 4 4 1 4] → L.eliminar_consecutivos() → L: [3 4 1 4]
'''


def eliminar_consecutivos(self):
    if self.prim is not None:
        actual = self.prim
        if actual.prox:
            siguiente = actual.prox
            while siguiente:
                if actual.dato == siguiente.dato:
                    actual.prox = siguiente.prox
                    siguiente = actual.prox
                    self.cant -= 1
                else:
                    actual = siguiente
                    siguiente = actual.prox


#129
'''
Implementar el método swap para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Éste recibe dos números positivos que representan posiciones y debe modificar la lista intercambiando los valores
ubicados en dichas posiciones. En caso de que los índices recibidos por parámetro excedan la longitud de la lista,
se debe lanzar una excepción del tipo IndexError. Ejemplo: Si L es [1,3,2,6,4], L.swap(1,3) dejará la lista como [1,6,2,3,4].
'''
def swap(self, indice_a, indice_b):
    if self.len < indice_b:
            raise IndexError('Se exedió del largo de la lista')
        indice = 0
        actual = self.primero
        while actual:
            if indice == indice_a:
                primer_cambio = actual.dato

            if indice == indice_b:
                segundo_cambio = actual.dato

            actual = actual.prox
            indice += 1

        indice = 0
        actual = self.primero
        while actual:

            if indice == indice_a:
                actual.dato = segundo_cambio
            if indice == indice_b:
                actual.dato = primer_cambio

            actual = actual.prox
            indice += 1


#130
'''
Implementar un método para una implementación de ListaEnlazada con referencia únicamente al primer nodo que devuelve una nueva
lista enlazada compuesta por los elementos que se encuentran en las posiciones impares de la original. Por ejemplo, para L = [3,1,6,8,9] el método debe devolver [1,8].
'''


def posiciones_impares(self):
    res = ListaEnlazada()
    actual = self.prim
    posicion = 0
    while actual:
        if posicion % 2 == 0:
            posicion += 1

        else:
            nuevo_nodo = _Nodo(actual.dato)
            if res.prim is None:
                res.prim = nuevo_nodo
                res_actual = res.prim
                posicion += 1

            else:
                res_actual.prox = nuevo_nodo
                res_actual = res_actual.prox
                posicion += 1

        actual = actual.prox
    return res


#131
'''
Implementar el método downsample(k) para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Este método debe eliminar todo elemento de la lista que ocupe una posición que no sea múltiplo del número k pasado por parámetro (k > 1).
Ejemplos:

L: [0, 1, 2, 3, 4, 5]                  → L.downsample(2) → L: [0, 2, 4]
L: ['a', 'b', 'c', 'd', 'e', 'f', 'g'] → L.downsample(4) → L: ['a', 'e']
'''


def downsample(self, k):
    if k <= 1:
        raise ValueError("El valor de k debe ser mayor a 1.")
    posicion = 1
    anterior = self.prim
    actual = anterior.prox
    while actual:
        if posicion % k != 0:
            anterior.prox = actual.prox
        else:
            anterior = actual
        actual = actual.prox
        posicion += 1
#132
'''
Implementar un método para una implementación de ListaEnlazada con referencia únicamente al primer nodo que reciba
una secuencia de números ordenados y sin repeticiones (por ejemplo, la tupla (0, 2, 6, 8)), y elimine los elementos
de la lista enlazada en dichas posiciones, recorriendo la lista enlazada una única vez. Si la secuencia de índices
a eliminar contiene una posición no válida se deberá lanzar una excepción. Ejemplos:

L: [ a b c d e ]  →  L.eliminar_posiciones([1, 3])  →  L: [ a c e ]
L: [ a c e ]      →  L.eliminar_posiciones([0, 2])  →  L: [ c ]
L: [ a c e ]      →  L.eliminar_posiciones([0, 3])  →  IndexError
'''
#133
'''
Implementar el método merge() para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Éste método recibe otra ListaEnlazada por parámetro y tiene como precondición que ambas tienen a todos sus elementos ordenados.
El método debe devolver una nueva lista enlazada que contenga a los elementos de las dos en orden. Ejemplos:

L1: [3,5,9], L2: [1,2,6,10] -> [1,2,3,5,6,9,10]
'''
def merge(self, lista_2):

    resultado = ListaEnlazada()

    act_l1 = self.prim
    act_l2 = lista_2.prim

    if not act_l1 and not act_l2:
        return resultado  #  Lista vacia

    act_res = None
    while act_l1 and act_l2:
        if act_l1.dato < act_l2.dato:
            nuevo = Nodo(act_l1.dato)
            act_l1 = act_l1.prox
        else:
            nuevo = Nodo(act_l2.dato)
            act_l2 = act_l2.prox

        if not act_res:
            act_res = nuevo
            resultado.prim = act_res
        else:
            act_res.prox = nuevo
            act_res = act_res.prox

    act_faltante = act_l1
    if act_l2:
        act_faltante = act_l2

    while act_faltante:
        nuevo = Nodo(act_faltante.dato)
        if not act_res:
            act_res = nuevo
            resultado.prim = act_res
        else:
            act_res.prox = nuevo
            act_res = act_res.prox

        act_faltante = act_faltante.prox

    return resultado
#134
'''
Implementar el método borrarUltimo para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
'''


def borrar_ultimo(self):
    actual = self.prim
    anterior = None
    while actual:
        if not actual.prox:
                anterior.prox = None
                actual = anterior
        else:
            anterior = actual
        actual = actual.prox
#135
'''
Para una implementación de ListaEnlazada con referencia únicamente al primer nodo implementar la primitiva suma_acumulativa()
que devuelva una nueva lista (del mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos de la lista original hasta el nodo i.
Por ejemplo: Si lista tiene los elementos 1, 2, 3, 4, lista.suma_acumulativa() devuelve una nueva ListaEnlazada con 1, 3, 6, 10.
'''


def suma_acumulativa(self):
    res = ListaEnlazada()
    actual = self.prim
    suma = actual.dato
    while actual:
        if res.prim is None:
            nuevo_nodo = _Nodo(suma)
            res.prim = nuevo_nodo
            res_actual = res.prim
        else:
            suma += actual.dato
            nuevo_nodo = _Nodo(suma)
            res_actual.prox = nuevo_nodo
            res_actual = res_actual.prox
        actual = actual.prox
    return res
#136
'''
Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo, se pide implementar el método filter,
que dada una función f que recibe un elemento y devuelve True o False, remueva todos los elementos de la lista para los
cuales la función devuelve False. (Aclaracion: el método modifica la lista, no devuelve una nueva ni tampoco utiliza
estructuras axuliar, y la funcion f se recibe por parametro)
'''
def filter(self, f):
    ant = None
    act = self.prim
    while act:
        if not f(act.dato):
            if not ant:
                self.prim = self.prim.prox
            else:
                ant.prox = act.prox
            self.len -= 1
        ant = act
        act = act.prox
#137
'''
Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo, se pide implementar el método __mul__
que reciba un número entero n y devuelva una nueva lista enlazada con los mismos elementos repetidos n veces.
Aclaración: la nueva lista debe ser recorrida una sola vez (es decir, no se puede utilizar el método append().
Ejemplo:
L: [a,b] → L * 3 → [a,b,a,b,a,b]
'''

#138
'''
Se tiene una clase ListaEnlazada cuya implementación cuenta únicamente con una referencia al primer nodo, que contiene
números ordenados de forma ascendente. Se pide escribir un método de la clase ListaEnlazada que la modifique eliminando
sus elementos repetidos. No se pueden utilizar otros métodos de la lista ni estructuras auxiliares.
'''


def eliminar_repetidos(self):
    actual = self.prim
    if actual.prox:
        siguiente = actual.prox
        while siguiente:
            if actual.dato == siguiente.dato:
                actual.prox = siguiente.prox
                siguiente = actual.prox
                self.cant -= 1
            else:
                actual = siguiente
                siguiente = actual.prox


#139
'''
Se tiene la clase ListaEnlazada implementada únicamente con una referencia al primer nodo. Implementar el método slice(inicio, fin)
que devuelve una nueva ListaEnlazada incluyendo sólo los elementos ubicados entre las posiciones inicio (inclusive) y fin (no inclusive).
La nueva lista enlazada debe ser recorrida una sola vez (es decir, no se puede usar el método append()).
Nota: En caso de que el valor de inicio sea menor a 0 toma los elementos a partir de la posición 0, y si el fin excede el largo de la lista,
toma los elementos hasta el final de la misma.
'''


def slice(self, inicio, fin):
    res = ListaEnlazada()
    actual = self.prim
    contador = 0
    if inicio < 0 and fin > self.cant - 1:
        while actual:
            nuevo_nodo = _Nodo(actual.dato)
            if res.prim is None:
                res.prim = nuevo_nodo
                res.actual = res.prim
                contador += 1
            else:
                if contador != self.cant - 1:
                    res.actual.prox = nuevo_nodo
                    res.actual = res.actual.prox
                    contador += 1
                else:
                    break
            actual = actual.prox

    if inicio >= 0 and fin > self.cant:
        while actual:
            nuevo_nodo = _Nodo(actual.dato)
            if contador < inicio:
                contador += 1
            else:
                if contador == inicio and res.prim is None:
                    res.prim = nuevo_nodo
                    res.actual = res.prim
                    contador += 1
                else:
                    if contador < fin - 1:
                        res.actual.prox = nuevo_nodo
                        res.actual = res.actual.prox
                        contador += 1
                    else:
                        break
            actual = actual.prox
    return res


#140
'''
Se cuenta con una clase ListaEnlazada, implementada con una referencia al primer nodo y la cantidad de elementos.
Implementar el método remover_todos(elemento), que recibe un elemento y remueve de la lista todas las apariciones del
mismo, devolviendo la cantidad de elementos removidos. Nota: Por razones de eficiencia, no se debe usar pop(), remove()
ni cualquier otro método de la lista que saque un elemento.
'''


def remover_todos(self, elemento):
    anterior = None
    actual = self.prim
    while actual:
        if actual.dato == elemento:
            self.cant -= 1
            if anterior is None:
                self.prim = actual.prox
            else:
                anterior.prox = actual.prox
        else:
            anterior = actual
        actual = actual.prox


#141
'''
Implementar el método clonar de la clase ListaEnlazada, que devuelve una nueva ListaEnlazada con los mismos elementos que la lista original.
La clase está conformada por una referencia al primer nodo (prim) y la cantidad de elementos (len).
'''


def clonar(self):
    res = ListaEnlazada()
    actual = self.prim
    res.prim = None
    while actual:
        nuevo_nodo = _Nodo(actual.dato)
        res.cant += 1
        if res.prim is None:
            res.prim = nuevo_nodo
            res_actual = res.prim

        else:
            res_actual.prox = nuevo_nodo
            res_actual = res_actual.prox

        actual = actual.prox
    return res


#142
'''
Implementar una clase ListaEnlazadaOrdenada que tenga un constructor y un método insertar_ordenado,
que recibe un elemento y lo inserta en la posición correspondiente. Asumir que los elementos pueden
compararse usando el operador <. Es decir, si x < y, el elemento x debe ser
insertado en la lista antes que el elemento y. Asumir que la clase _Nodo ya está implementada.
'''
#143
'''
Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva.
Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0.
La implementación de LE contiene una referencia al primer nodo y un atributo con la longitud. Ejemplo: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (len = 8)

le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]
'''


def rotar(self, n):
    n = n % self.cant
    if n == 0:
        return

    indice = 0
    actual = self.prim
    primero_en_mover = actual
    while actual:
        if indice + 1 == n:
            ultimo_en_mover = actual

        if indice == n:
            ultimo_en_mover.prox = None
            self.prim = actual

        if indice + 1 == self.cant:
            actual.prox = primero_en_mover
        indice += 1
        actual = actual.prox

#144
'''
Implementar para la ListaEnlazada el método distribuir_en_colas(k),
que recibe por parámetro un número entero k mayor a 1.
Este nuevo método debe devolver k nuevas colas con los elementos
de la lista distribuidos de forma alternada, respetando el orden
relativo de los elementos (los k elementos que están al principio
de la lista quedarían al frente de cada una de las colas).

Ejemplos:

L = [a b c d e f g] → L.distribuir(3) →
        [Cola([a d g]), Cola([b e]), Cola([c f])]
L = [a b c] → L.distribuir(4) →
        [Cola([a]), Cola([b]), Cola([c]), Cola([])]
'''

def distruibuir_en_colas(self, k):
    colas = [Cola() for _ in range(k)]

    actual = self.prim
    i = 0

    while actual:
        colas[i % len(colas)].encolar(actual.dato)

        i += 1
        actual = actual.prox

    return colas
