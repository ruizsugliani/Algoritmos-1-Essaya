
class Cola:
    #
    # HACER: implementar los métodos
    #

    def __init__(self, k):
        '???'

    def encolar(self, dato):
        'lanza ColaLlenaError si no hay más lugar'

    def desencolar(self):
        'lanza ColaVaciaError si la cola está vacía'

class ColaVaciaError(Exception):
    pass

class ColaLlenaError(Exception):
    pass

def pruebas():
    # creamos una cola con capacidad K = 5
    c = Cola(5)

    for i in range(10):
        # la cola está vacía, desencolar() debe lanzar ColaVaciaError
        ok = False
        try:
            c.desencolar()
        except ColaVaciaError:
            ok = True
        assert ok

        # encolamos 4 elementos
        for i in range(4):
            c.encolar(i)

        # la cola está llena, encolar() debe lanzar ColaLlenaError
        ok = False
        try:
            c.encolar(5)
        except ColaLlenaError:
            ok = True
        assert ok

        # desencolamos los 4 elementos
        for i in range(4):
            assert c.desencolar() == i

        # la cola está vacía, desencolar() debe lanzar ColaVaciaError
        ok = False
        try:
            c.desencolar()
        except ColaVaciaError:
            ok = True
        assert ok

        # encolamos y desencolamos para desplazar el inicio
        c.encolar(1)
        assert c.desencolar() == 1


    # OPCIONAL: agregar más casos de prueba.

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
