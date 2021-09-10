class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def __str__(self):
        res = ""
        act = self.prim
        while act:
            res += str(act.dato)
            act = act.prox
        res_f = "] -> [".join(res)
        return f"[{res_f}]"

    def esta_ordenada(self):
        actual = self.prim
        if not actual.prox:
            return True

        if actual.prox.dato < actual.dato:
            return False
        else:
            self.prim = actual.prox
            return self.esta_ordenada()

def pruebas():

    # creamos "a mano" la lista [3] -> [5] -> [8] -> [11]
    n3 = _Nodo(11, None)
    n2 = _Nodo(8, n3)
    n1 = _Nodo(5, n2)
    n0 = _Nodo(3, n1)
    lista = ListaEnlazada()
    lista.prim = n0

    assert lista.esta_ordenada()

    # OPCIONAL: Pruebas adicionales. Sugerencias:
    # - Repetir la prueba con una lista desordenada, y verificar que la
    #   función devuelve False
    # - Repetir la prueba con una lista vacía (es indistinto lo que devuelve
    #   la funcion, pero no debería fallar)


    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
