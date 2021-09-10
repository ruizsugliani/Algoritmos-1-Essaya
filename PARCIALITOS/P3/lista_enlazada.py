def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def __str__(self):
        res = ""
        act = self.prim
        while act:
            res += str(act.dato)
            act = act.prox
        res_f = "] -> [".join(res)
        return f"[{res_f}]"

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    '''
    Para una implementación de una ListaEnlazada que posee únicamente una referencia
    únicamente al primer nodo, se pide implementar una nueva primitiva que modifique
    la lista de tal forma que el menor elemento se encuentre al comienzo de la misma,
    manteniendo el orden relativo del resto de los elementos.
    Importante: El método no debe recorrer la lista más de una vez.
    Ejemplos:
    3 -> 5 -> 4 -> 2 -> 1   =>   1 -> 3 -> 5 -> 4 -> 2
    5 -> 6 -> 2 -> 3 -> 7   =>   2 -> 5 -> 6 -> 3 -> 7
    3 -> 4 -> 5 -> 6 -> 7   =>   3 -> 4 -> 5 -> 6 -> 7
    '''
    def menor_primero(self):
        menor = self.prim
        anterior = self.prim
        actual = anterior.prox
        while actual:
            if actual.dato < menor.dato:
                menor = actual
                self.prim = menor
                anterior.prox = actual.prox
            actual = actual.prox

l = ListaEnlazada()

l.append(3)
l.append(5)
l.append(4)
l.append(2)
l.append(1)

print(l)
l.menor_primero()
print(l)
