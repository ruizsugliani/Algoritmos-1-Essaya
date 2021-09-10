class ListaCircular:
    
    def append(self, dato):
        actual = self.prim
        if actual:
            while actual.prox != self.prim:
                actual = actual.prox
            actual.prox = _Nodo(dato, self.prim)
        
        else:
            self.prim = _Nodo(dato, self.prim)
            actual = self.prim
            actual.prox = self.prim
        self.cant += 1
   
    def pop(self, i=None):
        if i == None:
            i = self.cant - 1
        else:
            i %= self.cant
            
        nodo_anterior = self.prim
        nodo_actual = nodo_anterior.prox

        for _ in range((i - 1) if i != 0 else (self.cant - 1)):
            nodo_anterior = nodo_actual
            nodo_actual = nodo_anterior.prox

        dato = nodo_actual.dato
        
        if nodo_actual != self.prim:
            nodo_anterior.prox = nodo_actual.prox
        else:
            nodo_anterior.prox = self.prim.prox
            self.prim = nodo_anterior.prox

        self.cant -= 1
        return dato

    def insert(self, i, x):
        """
        Agrega el elemento `x` en la posicion `i` de la lista circular.
        Es posible introducir indices fuera de rango.
        """
        i %= (self.cant + 1)

        nodo_anterior = self.prim

        for _ in range((i - 1) if i != 0 else (self.cant - 1)):
            nodo_anterior = nodo_anterior.prox
        
        if i == 0:
            if self.prim:
                self.prim = _Nodo(x, self.prim)
                nodo_anterior.prox = self.prim
            else:
                self.prim = _Nodo(x)
                self.prim.prox = self.prim

        else:
            nodo_anterior.prox = _Nodo(x, nodo_anterior.prox)

        self.cant += 1

    def remove(self, x):
        """
        Elimina la primera aparicion del elemento `x` pasado como argumento.
        Si `x` no esta en la lista levanta `ValueError`.
        """
        if not self.prim:
            raise ValueError

        nodo_anterior = self.prim
        nodo_actual = nodo_anterior.prox

        if self.prim.dato == x:
            for _ in range(self.cant - 1):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.prox
        else:
            for _ in range(self.cant - 1):
                if nodo_actual.dato == x:
                    break
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.prox

        if nodo_actual.dato != x:
            raise ValueError

        if nodo_actual == self.prim:
            if self.cant == 1:
                self.prim.prox = None
            nodo_anterior.prox = self.prim.prox
            self.prim = self.prim.prox
        else:
            nodo_anterior.prox = nodo_actual.prox

        self.cant -= 1

    def __len__(self):
        return self.cant

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

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

l = ListaCircular()
l.append(1)
l.append(2)

print(l)