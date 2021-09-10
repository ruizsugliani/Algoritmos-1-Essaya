class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0
#EJERCICIO 1
    def __str__(self):
        res = ""
        act = self.prim
        while act:
            res += str(act.dato)
            act = act.prox
        res_f = "] -> [".join(res)
        return f"[{res_f}]"
#EJERCICIO 4
    def extend(self, lista_aux):
        if self.prim is None:
            self.prim = lista_aux.prim
            self.cant = lista_aux.cant

        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox

            actual_aux = lista_aux.prim
            while actual_aux:
                actual.prox = _Nodo(actual_aux.dato)
                actual = actual.prox
                self.cant += 1
                actual_aux = actual_aux.prox

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

    def __len__(self):
        return self.cant
#EJERCICIO 3
    def insert(self, i, x):
        posicion = 0
        nuevo = _Nodo(x)

        if i > self.cant or i < 0:
            raise IndexError

        elif not self.prim:
            self.prim = nuevo

        elif i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo

        else:
            actual = self.prim
            while posicion < i - 1:
                actual = actual.prox
                posicion += 1
            nuevo.prox = actual.prox
            actual.prox = nuevo
        self.cant += 1
#EJERCICIO 7
    def filter(self, f):
        actual = self.prim
        res = ListaEnlazada()
        while actual:
            if f(actual.dato):
                if res.prim is None:
                    nuevo_nodo = _Nodo(actual.dato)
                    res.prim = nuevo_nodo
                    actual_res = res.prim
                    res.cant += 1
            
                else:
                    nuevo_nodo = _Nodo(actual.dato)
                    actual_res.prox = nuevo_nodo
                    actual_res = actual_res.prox
                    res.cant += 1
            
            actual = actual.prox
        return res
#EJERCICIO 6
    def duplicar(self, elem):
        actual = self.prim
        while actual:
            if actual.dato == elem:
                nuevo_nodo = _Nodo(actual.dato)
                siguiente = nuevo_nodo
                siguiente.prox = actual.prox
                actual.prox = siguiente
                actual = siguiente.prox
                self.cant += 1
            else:
                actual = actual.prox 
#EJERCICIO 8
    def invertir(self):
        ant = None
        act = self.prim
        while act:
            sig = act.prox
            act.prox = ant
            ant = act
            act = sig
        self.prim = ant
#EJERCICIO 2
    def pop(self, i=None):    
        if i is None:
            i = self.cant - 1

        if i < 0 or i >= self.cant:
            raise IndexError

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox

        else:
            anterior = self.prim
            actual = anterior.prox
            for pos in range(1, i):
                anterior = actual
                actual = anterior.prox
            dato = actual.dato
            anterior.prox = actual.prox
        self.cant -= 1
        return dato
#EJERCICIO 5
    def remover_todos(self, elem):
        anterior = None
        actual = self.prim
        removidos = 0
        while actual:
            if actual.dato == elem:
                removidos += 1
                self.cant -= 1
                if not anterior:
                    self.prim = actual.prox
                
                else:
                    anterior.prox = actual.prox
                    
            else:
                anterior = actual
            actual = actual.prox
        return removidos

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
