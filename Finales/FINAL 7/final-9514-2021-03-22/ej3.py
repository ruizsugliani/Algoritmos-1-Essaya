
class Nodo:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

#
# HACER: implementar la función
#
def crear_arbol(s):

def pruebas():
    raiz = crear_arbol("abc..d..e..")

    #       a   <--- raiz
    #     /  \
    #    b    e
    #  /  \
    # c   d

    assert raiz.dato == 'a'
    assert raiz.izq.dato == 'b'
    assert raiz.der.dato == 'e'
    assert raiz.izq.izq.dato == 'c'
    assert raiz.izq.der.dato == 'd'

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
