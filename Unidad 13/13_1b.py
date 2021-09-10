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