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