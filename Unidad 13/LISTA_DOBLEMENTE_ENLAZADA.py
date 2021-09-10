class ListaDobleEnlazada:
    
    def append(self, dato):
        nuevo_nodo = _Nodo(dato)
        if self.prim is None:
            self.prim = nuevo_nodo
        else:
            actual = self.prim
            while actual.prox:
                actual.ant = actual
                actual = actual.prox 
            actual.prox = nuevo_nodo
            nuevo_nodo.ant = actual
            self.cant += 1


    def pop(self, i=None):
        '''
        DOC: Completar
        '''


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
    def __init__(self, dato, prox=None, ant=None):
        self.dato = dato
        self.prox = prox
        self.ant = ant

l = ListaDobleEnlazada
l.append(1)