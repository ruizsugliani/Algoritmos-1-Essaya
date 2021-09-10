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