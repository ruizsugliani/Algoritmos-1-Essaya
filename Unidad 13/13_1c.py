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
            actual.prox =  nuevo
        self.cant += 1