def remove(self, x):
        if self.prim.dato == x:
            self.prim = self.prim.prox

        else:
            nodo_anterior = self.prim
            nodo_actual = nodo_anterior.prox

            while nodo_actual != None and nodo_actual.dato != x:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.prox

            if nodo_actual == None:
                raise ValueError("El valor no está en la lista.")

            nodo_anterior.prox = nodo_actual.prox

        self.cant -= 1