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